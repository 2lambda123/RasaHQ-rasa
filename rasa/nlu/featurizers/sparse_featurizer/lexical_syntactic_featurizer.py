from __future__ import annotations
import logging
from collections import OrderedDict

import scipy.sparse
import numpy as np
from typing import (
    Any,
    Dict,
    Text,
    List,
    Tuple,
    Hashable,
    Callable,
    Set,
)

from rasa.engine.graph import ExecutionContext, GraphComponent
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.nlu.tokenizers.spacy_tokenizer import POS_TAG_KEY, SpacyTokenizer
from rasa.nlu.tokenizers.tokenizer import Token
from rasa.nlu.tokenizers.tokenizer import Tokenizer
from rasa.nlu.featurizers.sparse_featurizer.sparse_featurizer import SparseFeaturizer2
from rasa.nlu.constants import TOKENS_NAMES
from rasa.shared.constants import DOCS_URL_COMPONENTS
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import TEXT
from rasa.shared.exceptions import InvalidConfigException
import rasa.shared.utils.io
import rasa.utils.io
from rasa.nlu.featurizers.sparse_featurizer._lexical_syntactic_featurizer import (
    LexicalSyntacticFeaturizer,
)

logger = logging.getLogger(__name__)

# TODO: remove after all references to old featurizer have been removed
LexicalSyntacticFeaturizer = LexicalSyntacticFeaturizer


class LexicalSyntacticFeaturizerGraphComponent(SparseFeaturizer2, GraphComponent):
    """Extracts and encodes lexical syntactic features.

    Given a sequence of tokens, this featurizer produces a sequence of features
    where the `t`-th feature encodes lexical and syntactic information about the `t`-th
    token and it's surrounding tokens.

    In detail: The lexical syntactic features can be specified via a list of
    configurations `[c_0, c_1, ..., c_n]` where each `c_i` is a list of names of
    lexical and syntactic features (e.g. `low`, `suffix2`, `digit`).
    For a given tokenized text, the featurizer will consider a window of size `n`
    around each token and evaluate the given list of configurations as follows:
    - It will extract the features listed in `c_m` where `m = (n-1)/2` if n is even and
      `n/2` from token `t`
    - It will extract the features listed in `c_{m-1}`,`c_{m-2}` ... ,  from the last,
      second to last, ... token before token `t`, respectively.
    - It will extract the features listed `c_{m+1}`, `c_{m+1}`, ... for the first,
      second, ... token `t`, respectively.
    It will then combine all these features into one feature for position `t`.

    Example:
      If we specify [['low'], ['upper'], ['prefix2']], then for each position `t`
      the `t`-th feature will encode whether the token at position `t` is upper case,
      where the token at position `t-1` is lower case and the first two characters
      of the token at position `t+1`.
    """

    FILENAME_FEATURE_TO_IDX_DICT = "feature_to_idx_dict.pkl"

    END_OF_SENTENCE = "EOS"
    BEGIN_OF_SENTENCE = "BOS"

    FEATURES = "features"

    # NOTE: "suffix5" of the token "is" will be "is". Hence, when combining multiple
    # prefixes, short words will be represented/encoded repeatedly.
    _FUNCTION_DICT: Dict[Text, Callable[[Token], Hashable]] = {
        "low": lambda token: token.text.islower(),
        "title": lambda token: token.text.istitle(),
        "prefix5": lambda token: token.text[:5],
        "prefix2": lambda token: token.text[:2],
        "suffix5": lambda token: token.text[-5:],
        "suffix3": lambda token: token.text[-3:],
        "suffix2": lambda token: token.text[-2:],
        "suffix1": lambda token: token.text[-1:],
        "pos": lambda token: token.data.get(POS_TAG_KEY, None),
        "pos2": lambda token: token.data.get(POS_TAG_KEY, [])[:2]
        if POS_TAG_KEY in token.data
        else None,
        "upper": lambda token: token.text.isupper(),
        "digit": lambda token: token.text.isdigit(),
    }

    SUPPORTED_FEATURES = sorted(
        set(_FUNCTION_DICT.keys()).union([END_OF_SENTENCE, BEGIN_OF_SENTENCE])
    )

    @classmethod
    def _extract_raw_features_from_token(
        cls, feature_name: Text, token: Token, token_position: int, num_tokens: int,
    ) -> Hashable:
        """Extracts a raw feature from the token at the given position.

        Args:
          feature_name: the name of a supported feature
          token: the token from which we want to extract the feature
          token_position: the position of the token inside the tokenized text
          num_tokens: the total number of tokens in the tokenized text
        Returns:
          the raw feature value
        """
        if feature_name not in cls.SUPPORTED_FEATURES:
            raise ValueError(
                f"Configured feature '{feature_name}' not valid. Please check "
                f"'{DOCS_URL_COMPONENTS}' for valid configuration parameters."
            )
        if feature_name == cls.END_OF_SENTENCE:
            return token_position == num_tokens - 1
        if feature_name == cls.BEGIN_OF_SENTENCE:
            return token_position == 0
        return cls._FUNCTION_DICT[feature_name](token)

    @staticmethod
    def get_default_config() -> Dict[Text, Any]:
        """Returns the component's default config."""
        return {
            **SparseFeaturizer2.get_default_config(),
            LexicalSyntacticFeaturizerGraphComponent.FEATURES: [
                ["low", "title", "upper"],
                ["BOS", "EOS", "low", "upper", "title", "digit"],
                ["low", "title", "upper"],
            ],
        }

    def __init__(
        self,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> None:
        """Instantiates a new `LexicalSyntacticFeaturizer` instance."""
        super().__init__(config)
        # graph component
        self._model_storage = model_storage
        self._resource = resource
        self._execution_context = execution_context
        # featurizer specific
        self._feature_config = self._config.get(self.FEATURES, [])
        self._feature_to_idx_dict = {}
        self._number_of_features = -1
        # where the negative value indicates that feature_to_idx hasn't been set yet

    def validate_config(self) -> None:
        """Validates that the component is configured properly."""
        super().validate_config()
        feature_config = self._config.get(self.FEATURES, [])
        if not feature_config:
            rasa.shared.utils.io.raise_warning(
                f"Expected 'features' to be configured for the "
                f"{self.__class__.__name__} {self._identifier}. ",
                doc=DOCS_URL_COMPONENTS,
            )
            feature_config = []  # in case it was None
        message = (
            f"Expected configuration of `features` to be a list of lists that "
            f"that contain names of lexical and syntactic features "
            f" (i.e. {self.SUPPORTED_FEATURES})."
            f"Received {feature_config} instead. "
        )
        try:
            configured_feature_names = set(
                feature_name
                for pos_config in feature_config
                for feature_name in pos_config
            )
        except TypeError as e:
            raise InvalidConfigException(message) from e
        if configured_feature_names.difference(self.SUPPORTED_FEATURES):
            raise InvalidConfigException(message)

    def validate_compatibility_with_tokenizer(self, tokenizer: Tokenizer) -> None:
        """Validate a configuration for this component in the context of a recipe."""
        # NOTE: this wasn't done before, there was just a comment
        # TODO: add (something like) this to graph validation
        configured_feature_names = set(
            feature_name
            for pos_config in self._feature_config
            for feature_name in pos_config
        )
        if any(
            feature_name in configured_feature_names for feature_name in ["pos", "pos2"]
        ) and not isinstance(tokenizer, SpacyTokenizer):
            rasa.shared.utils.io.raise_warning(
                f"Expected tokenizer to be {SpacyTokenizer.__name__} "
                f"because the given configuration includes part-of-speech features "
                f"`pos` and/or `pos2` which can only be extracted from tokens "
                f"produced by this tokenizer. "
                f"Continuing without the part-of-speech-features."
            )

    def _set(
        self,
        feature_to_idx_dict: Dict[Text, Dict[Text, Hashable]],
        check_consistency_with_config: bool = False,
    ) -> None:
        """Sets the "feature" to index mapping.

        Here, "feature" denotes the combination of window position, feature name,
        and feature_value.

        Args:
          feature_to_idx_dict: mapping from tuples of window position and feature name
            to a mapping from feature values to indices
          check_consistency_with_config: whether the consistency with the current
            `self.config` should be checked
        """
        self._feature_to_idx_dict = feature_to_idx_dict
        self._number_of_features = sum(
            [
                len(feature_values.values())
                for feature_values in self._feature_to_idx_dict.values()
            ]
        )
        if check_consistency_with_config:
            # used during load()
            known_features = set(self._feature_to_idx_dict.keys())
            not_in_config = known_features.difference(self._config.keys())
            if not_in_config:
                rasa.shared.utils.io.raise_warning(
                    f"A feature to index mapping has been loaded that does not match "
                    f"the configured features. The given mapping configures "
                    f" (position in window, feature_name): {not_in_config}. "
                    f" These are not specified in the given config {self._config}. "
                    f" Will continue without these features."
                )

    def train(self, training_data: TrainingData,) -> Resource:
        """Trains the featurizer.

        Args:
          training_data: the training data
        """
        feature_to_idx_dict = self._create_feature_to_idx_dict(training_data)
        self._set(feature_to_idx_dict=feature_to_idx_dict)
        self.persist()
        return self._resource

    def _create_feature_to_idx_dict(
        self, training_data: TrainingData
    ) -> Dict[Tuple[int, Text], Dict[Hashable, int]]:
        """Create a nested dictionary of all feature values.

        Returns:
           a nested mapping that maps from tuples of positions (in the window) and
           supported feature names to "raw feature to index" mappings, i.e.
           mappings that map the respective raw feature values to unique indices
           (where `unique` means unique with respect to all indices in the
           *nested* mapping)
        """
        # collect all raw feature values
        feature_vocabulary: Dict[Text, Set[Hashable]] = dict()
        for example in training_data.training_examples:
            tokens = example.get(TOKENS_NAMES[TEXT], [])
            sentence_features = self._map_tokens_to_raw_features(tokens)
            for token_features in sentence_features:
                for position_and_feature_name, feature_value in token_features.items():
                    feature_vocabulary.setdefault(position_and_feature_name, set()).add(
                        feature_value
                    )
        # assign a unique index to each feature value
        return self._build_feature_to_index_map(feature_vocabulary)

    def _map_tokens_to_raw_features(
        self, tokens: List[Token]
    ) -> List[Dict[Tuple[int, Text], Hashable]]:
        """Extracts the raw feature values.

        Args:
          tokens: a tokenized text
        Returns:
          a list of feature dictionaries for each token in the given list
          where each feature dictionary maps a tuple containing
          - a position (in the window) and
          - a supported feature name
          to the corresponding raw feature value
        """
        sentence_features = []

        for anchor in range(len(tokens)):

            # in case of an even number we will look at one more word before,
            # e.g. window size 4 will result in a window range of
            # [-2, -1, 0, 1] (0 = current word in sentence)
            window_size = len(self._feature_config)
            half_window_size = window_size // 2
            window_range = range(-half_window_size, half_window_size + window_size % 2)
            assert len(window_range) == window_size

            token_features: Dict[Tuple[int, Text], Hashable] = {}

            for window_position, relative_position in enumerate(window_range):
                absolute_position = anchor + relative_position

                # skip, if current_idx is pointing to a non-existing token
                if absolute_position < 0 or absolute_position >= len(tokens):
                    continue

                token = tokens[absolute_position]
                for feature_name in self._feature_config[window_position]:
                    token_features[
                        (window_position, feature_name)
                    ] = self._extract_raw_features_from_token(
                        token=token,
                        feature_name=feature_name,
                        token_position=absolute_position,
                        num_tokens=len(tokens),
                    )

            sentence_features.append(token_features)

        return sentence_features

    @staticmethod
    def _build_feature_to_index_map(
        feature_vocabulary: Dict[Tuple[int, Text], Set[Text]]
    ) -> Dict[Tuple[int, Text], Dict[Hashable, int]]:
        """Creates a nested dictionary for mapping raw features to indices.

        Args:
          feature_vocabulary: a mapping from tuples of positions (in the window) and
            supported feature names to the set of possible feature values
        Returns:
           a nested mapping that maps from tuples of positions (in the window) and
           supported feature names to "raw feature to index" mappings, i.e.
           mappings that map the respective raw feature values to unique indices
           (where `unique` means unique with respect to all indices in the
           *nested* mapping)
        """
        # Note that this will only sort the top level keys - and we keep
        # doing it to ensure consistently with what was done before)
        feature_vocabulary = OrderedDict(sorted(feature_vocabulary.items()))

        # create the nested mapping
        feature_to_idx_dict: Dict[Tuple[int, Text], Dict[Hashable, int]] = {}
        offset = 0
        for position_and_feature_name, feature_values in feature_vocabulary.items():
            feature_to_idx_dict[position_and_feature_name] = {
                feature_value: feature_idx
                for feature_idx, feature_value in enumerate(
                    sorted(feature_values), start=offset
                )
            }
            offset += len(feature_values)

        return feature_to_idx_dict

    def process(self, messages: List[Message]) -> List[Message]:
        """Featurizes all given messages in-place.

        Returns:
          the given list of messages which have been modified in-place
        """
        for message in messages:
            self.process_message(message)
        return messages

    def process_message(self, message: Message) -> None:
        """Featurize the given message in-place.

        Args:
          message: a message to be featurized
        """
        if self._number_of_features < 0:
            rasa.shared.utils.io.raise_warning(
                f"The {self.__class__.__name__} {self._identifier} has not been "
                f"trained yet. "
                f"Continuing without adding features from this featurizer."
            )
            return
        if not self._feature_to_idx_dict:
            rasa.shared.utils.io.raise_warning(
                f"The {self.__class__.__name__} {self._identifier} has been "
                f"trained but no features have been identified. "
                f"Continuing without adding features from this featurizer."
            )
            return
        tokens = message.get(TOKENS_NAMES[TEXT])
        if tokens:
            sentence_features = self._map_tokens_to_raw_features(tokens)
            sparse_matrix = self._map_raw_features_to_indices(sentence_features)
            self.add_features_to_message(
                # FIXME: create sentence feature and make `sentence` non optional
                sequence=sparse_matrix,
                sentence=None,
                attribute=TEXT,
                message=message,
            )

    def _map_raw_features_to_indices(
        self, sentence_features: List[Dict[Text, Any]]
    ) -> scipy.sparse.coo_matrix:
        """Converts the raw features to one-hot encodings.

        Requires the "feature" to index dictionary, i.e. the featurizer must have
        been trained.

        Args:
          sentence_features: a list of feature dictionaries where the `t`-th feature
            dictionary maps a tuple containing
            - a position (in the window) and
            - a supported feature name
            to the raw feature value extracted from the window around the `t`-th token.

        Returns:
           a sparse matrix where the `i`-th row is a multi-hot vector that encodes the
           raw features extracted from the window around the `i`-th token
        """
        if self._number_of_features < 0:
            raise RuntimeError("Expected the featurizer to be trained.")
        rows = []
        cols = []
        shape = (len(sentence_features), self._number_of_features)
        for token_idx, token_features in enumerate(sentence_features):
            for position_and_feature_name, feature_value in token_features.items():
                mapping = self._feature_to_idx_dict.get(position_and_feature_name)
                if not mapping:
                    continue
                feature_idx = mapping.get(feature_value, -1)
                if feature_idx > -1:
                    rows.append(token_idx)
                    cols.append(feature_idx)
        rows = np.array(rows)
        cols = np.array(cols)
        data = np.ones(len(rows))
        return scipy.sparse.coo_matrix((data, (rows, cols)), shape=shape)

    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> LexicalSyntacticFeaturizerGraphComponent:
        """Creates a new untrained component (see parent class for full docstring)."""
        return cls(config, model_storage, resource, execution_context)

    @classmethod
    def load(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
        **kwargs: Any,
    ) -> LexicalSyntacticFeaturizerGraphComponent:
        """Loads trained component (see parent class for full docstring)."""
        try:
            with model_storage.read_from(resource) as model_path:
                feature_to_idx_dict = rasa.utils.io.json_unpickle(
                    model_path / cls.FILENAME_FEATURE_TO_IDX_DICT, keys=True
                )
                loaded_featurizer = cls(
                    config=config,
                    model_storage=model_storage,
                    resource=resource,
                    execution_context=execution_context,
                )
                loaded_featurizer._set(
                    feature_to_idx_dict, check_consistency_with_config=True
                )
                return loaded_featurizer
        except ValueError:
            logger.warning(
                f"Failed to load {cls.__class__.__name__} from model storage. Resource "
                f"'{resource.name}' doesn't exist."
            )
            return cls(config, model_storage, resource, execution_context)

    def persist(self) -> None:
        """Persist this model (see parent class for full docstring)."""
        if self._number_of_features < 0:  # i.e. was never trained
            return None

        with self._model_storage.write_to(self._resource) as model_path:
            rasa.utils.io.json_pickle(
                model_path / self.FILENAME_FEATURE_TO_IDX_DICT,
                self._feature_to_idx_dict,
                keys=True,
            )
