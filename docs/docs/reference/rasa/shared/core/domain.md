---
sidebar_label: rasa.shared.core.domain
title: rasa.shared.core.domain
---
## InvalidDomain Objects

```python
class InvalidDomain(RasaException)
```

Exception that can be raised when domain is not valid.

## ActionNotFoundException Objects

```python
class ActionNotFoundException(ValueError,  RasaException)
```

Raised when an action name could not be found.

## SessionConfig Objects

```python
class SessionConfig(NamedTuple)
```

The Session Configuration.

#### default

```python
 | @staticmethod
 | default() -> "SessionConfig"
```

Returns the SessionConfig with the default values.

#### are\_sessions\_enabled

```python
 | are_sessions_enabled() -> bool
```

Returns a boolean value depending on the value of session_expiration_time.

#### as\_dict

```python
 | as_dict() -> Dict
```

Return serialized `SessionConfig`.

## EntityProperties Objects

```python
@dataclass
class EntityProperties()
```

Class for keeping track of the properties of entities in the domain.

## Domain Objects

```python
class Domain()
```

The domain specifies the universe in which the bot&#x27;s policy acts.

A Domain subclass provides the actions the bot can take, the intents
and entities it can recognise.

#### empty

```python
 | @classmethod
 | empty(cls) -> "Domain"
```

Returns empty Domain.

#### load

```python
 | @classmethod
 | load(cls, paths: Union[List[Union[Path, Text]], Text, Path]) -> "Domain"
```

Returns loaded Domain after merging all domain files.

#### from\_path

```python
 | @classmethod
 | from_path(cls, path: Union[Text, Path]) -> "Domain"
```

Loads the `Domain` from a path.

#### from\_file

```python
 | @classmethod
 | from_file(cls, path: Text) -> "Domain"
```

Loads the `Domain` from a YAML file.

#### from\_yaml

```python
 | @classmethod
 | from_yaml(cls, yaml: Text, original_filename: Text = "") -> "Domain"
```

Loads the `Domain` from YAML text after validating it.

#### from\_dict

```python
 | @classmethod
 | from_dict(cls, data: Dict) -> "Domain"
```

Deserializes and creates domain.

**Arguments**:

- `data` - The serialized domain.
  

**Returns**:

  The instantiated `Domain` object.

#### from\_directory

```python
 | @classmethod
 | from_directory(cls, path: Text) -> "Domain"
```

Loads and merges multiple domain files recursively from a directory tree.

#### merge

```python
 | merge(domain: Optional["Domain"], override: bool = False) -> "Domain"
```

Merges this domain dict with another one, combining their attributes.

This method merges domain dicts, and ensures all attributes (like ``intents``,
``entities``, and ``actions``) are known to the Domain when the
object is created.

List attributes like ``intents`` and ``actions`` are deduped
and merged. Single attributes are taken from `domain1` unless
override is `True`, in which case they are taken from `domain2`.

#### merge\_domain\_dicts

```python
 | @staticmethod
 | merge_domain_dicts(domain_dict: Dict, combined: Dict, override: bool = False) -> Dict
```

Combines two domain dictionaries.

#### collect\_slots

```python
 | @staticmethod
 | collect_slots(slot_dict: Dict[Text, Any]) -> List[Slot]
```

Collects a list of slots from a dictionary.

#### retrieval\_intents

```python
 | @rasa.shared.utils.common.lazy_property
 | retrieval_intents() -> List[Text]
```

List retrieval intents present in the domain.

#### collect\_entity\_properties

```python
 | @classmethod
 | collect_entity_properties(cls, domain_entities: List[Union[Text, Dict[Text, Any]]]) -> EntityProperties
```

Get entity properties for a domain from what is provided by a domain file.

**Arguments**:

- `domain_entities` - The entities as provided by a domain file.
  

**Returns**:

  An instance of EntityProperties.

#### collect\_intent\_properties

```python
 | @classmethod
 | collect_intent_properties(cls, intents: List[Union[Text, Dict[Text, Any]]], entity_properties: EntityProperties) -> Dict[Text, Dict[Text, Union[bool, List]]]
```

Get intent properties for a domain from what is provided by a domain file.

**Arguments**:

- `intents` - The intents as provided by a domain file.
- `entity_properties` - Entity properties as provided by the domain file.
  

**Returns**:

  The intent properties to be stored in the domain.

#### \_\_init\_\_

```python
 | __init__(intents: Union[Set[Text], List[Text], List[Dict[Text, Any]]], entities: List[Union[Text, Dict[Text, Any]]], slots: List[Slot], responses: Dict[Text, List[Dict[Text, Any]]], action_names: List[Text], forms: Union[Dict[Text, Any], List[Text]], data: Dict, action_texts: Optional[List[Text]] = None, store_entities_as_slots: bool = True, session_config: SessionConfig = SessionConfig.default()) -> None
```

Creates a `Domain`.

**Arguments**:

- `intents` - Intent labels.
- `entities` - The names of entities which might be present in user messages.
- `slots` - Slots to store information during the conversation.
- `responses` - Bot responses. If an action with the same name is executed, it
  will send the matching response to the user.
- `action_names` - Names of custom actions.
- `forms` - Form names and their slot mappings.
- `data` - original domain dict representation.
- `action_texts` - End-to-End bot utterances from end-to-end stories.
- `store_entities_as_slots` - If `True` Rasa will automatically create `SlotSet`
  events for entities if there are slots with the same name as the entity.
- `session_config` - Configuration for conversation sessions. Conversations are
  restarted at the end of a session.

#### \_\_deepcopy\_\_

```python
 | __deepcopy__(memo: Optional[Dict[int, Any]]) -> "Domain"
```

Enables making a deep copy of the `Domain` using `copy.deepcopy`.

See https://docs.python.org/3/library/copy.html#copy.deepcopy
for more implementation.

**Arguments**:

- `memo` - Optional dictionary of objects already copied during the current
  copying pass.
  

**Returns**:

  A deep copy of the current domain.

#### count\_conditional\_response\_variations

```python
 | count_conditional_response_variations() -> int
```

Returns count of conditional response variations.

#### \_\_hash\_\_

```python
 | __hash__() -> int
```

Returns a unique hash for the domain.

#### fingerprint

```python
 | fingerprint() -> Text
```

Returns a unique hash for the domain which is stable across python runs.

**Returns**:

  fingerprint of the domain

#### user\_actions\_and\_forms

```python
 | @rasa.shared.utils.common.lazy_property
 | user_actions_and_forms() -> List[Text]
```

Returns combination of user actions and forms.

#### num\_actions

```python
 | @rasa.shared.utils.common.lazy_property
 | num_actions() -> int
```

Returns the number of available actions.

#### num\_states

```python
 | @rasa.shared.utils.common.lazy_property
 | num_states() -> int
```

Number of used input states for the action prediction.

#### retrieval\_intent\_responses

```python
 | @rasa.shared.utils.common.lazy_property
 | retrieval_intent_responses() -> Dict[Text, List[Dict[Text, Any]]]
```

Return only the responses which are defined for retrieval intents.

#### is\_retrieval\_intent\_response

```python
 | @staticmethod
 | is_retrieval_intent_response(response: Tuple[Text, List[Dict[Text, Any]]]) -> bool
```

Check if the response is for a retrieval intent.

These responses have a `/` symbol in their name. Use that to filter them from
the rest.

#### index\_for\_action

```python
 | index_for_action(action_name: Text) -> int
```

Looks up which action index corresponds to this action name.

#### raise\_action\_not\_found\_exception

```python
 | raise_action_not_found_exception(action_name_or_text: Text) -> NoReturn
```

Raises exception if action name or text not part of the domain or stories.

**Arguments**:

- `action_name_or_text` - Name of an action or its text in case it&#x27;s an
  end-to-end bot utterance.
  

**Raises**:

- `ActionNotFoundException` - If `action_name_or_text` are not part of this
  domain.

#### slot\_states

```python
 | @rasa.shared.utils.common.lazy_property
 | slot_states() -> List[Text]
```

Returns all available slot state strings.

#### entity\_states

```python
 | @rasa.shared.utils.common.lazy_property
 | entity_states() -> List[Text]
```

Returns all available entity state strings.

#### concatenate\_entity\_labels

```python
 | @staticmethod
 | concatenate_entity_labels(entity_labels: Dict[Text, List[Text]], entity: Optional[Text] = None) -> List[Text]
```

Concatenates the given entity labels with their corresponding sub-labels.

If a specific entity label is given, only this entity label will be
concatenated with its corresponding sub-labels.

**Arguments**:

- `entity_labels` - A map of an entity label to its sub-label list.
- `entity` - If present, only this entity will be considered.
  

**Returns**:

  A list of labels.

#### input\_state\_map

```python
 | @rasa.shared.utils.common.lazy_property
 | input_state_map() -> Dict[Text, int]
```

Provide a mapping from state names to indices.

#### input\_states

```python
 | @rasa.shared.utils.common.lazy_property
 | input_states() -> List[Text]
```

Returns all available states.

#### get\_active\_state

```python
 | get_active_state(tracker: "DialogueStateTracker", omit_unset_slots: bool = False) -> State
```

Given a dialogue tracker, makes a representation of current dialogue state.

**Arguments**:

- `tracker` - dialog state tracker containing the dialog so far
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A representation of the dialogue&#x27;s current state.

#### states\_for\_tracker\_history

```python
 | states_for_tracker_history(tracker: "DialogueStateTracker", omit_unset_slots: bool = False, ignore_rule_only_turns: bool = False, rule_only_data: Optional[Dict[Text, Any]] = None) -> List[State]
```

List of states for each state of the trackers history.

**Arguments**:

- `tracker` - Dialogue state tracker containing the dialogue so far.
- `omit_unset_slots` - If `True` do not include the initial values of slots.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  A list of states.

#### slots\_for\_entities

```python
 | slots_for_entities(entities: List[Dict[Text, Any]]) -> List[SlotSet]
```

Creates slot events for entities if from_entity mapping matches.

**Arguments**:

- `entities` - The list of entities.
  

**Returns**:

  A list of `SlotSet` events.

#### persist\_specification

```python
 | persist_specification(model_path: Text) -> None
```

Persist the domain specification to storage.

#### load\_specification

```python
 | @classmethod
 | load_specification(cls, path: Text) -> Dict[Text, Any]
```

Load a domains specification from a dumped model directory.

#### compare\_with\_specification

```python
 | compare_with_specification(path: Text) -> bool
```

Compare the domain spec of the current and the loaded domain.

Throws exception if the loaded domain specification is different
to the current domain are different.

#### as\_dict

```python
 | as_dict() -> Dict[Text, Any]
```

Return serialized `Domain`.

#### get\_responses\_with\_multilines

```python
 | @staticmethod
 | get_responses_with_multilines(responses: Dict[Text, List[Dict[Text, Any]]]) -> Dict[Text, List[Dict[Text, Any]]]
```

Returns `responses` with preserved multilines in the `text` key.

**Arguments**:

- `responses` - Original `responses`.
  

**Returns**:

  `responses` with preserved multilines in the `text` key.

#### persist

```python
 | persist(filename: Union[Text, Path]) -> None
```

Write domain to a file.

#### as\_yaml

```python
 | as_yaml() -> Text
```

Dump the `Domain` object as a YAML string.

This function preserves the orders of the keys in the domain.

**Returns**:

  A string in YAML format representing the domain.

#### intent\_config

```python
 | intent_config(intent_name: Text) -> Dict[Text, Any]
```

Return the configuration for an intent.

#### intents

```python
 | @rasa.shared.utils.common.lazy_property
 | intents() -> List[Text]
```

Returns sorted list of intents.

#### entities

```python
 | @rasa.shared.utils.common.lazy_property
 | entities() -> List[Text]
```

Returns sorted list of entities.

#### domain\_warnings

```python
 | domain_warnings(intents: Optional[Union[List[Text], Set[Text]]] = None, entities: Optional[Union[List[Text], Set[Text]]] = None, actions: Optional[Union[List[Text], Set[Text]]] = None, slots: Optional[Union[List[Text], Set[Text]]] = None) -> Dict[Text, Dict[Text, Set[Text]]]
```

Generate domain warnings from intents, entities, actions and slots.

Returns a dictionary with entries for `intent_warnings`,
`entity_warnings`, `action_warnings` and `slot_warnings`. Excludes domain slots
from domain warnings in case they are not featurized.

#### utterances\_for\_response

```python
 | @property
 | utterances_for_response() -> Set[Text]
```

Returns utterance set which should have a response.

Will filter out utterances which are subintent (retrieval intent) types.
eg. if actions have [&#x27;utter_chitchat&#x27;, &#x27;utter_chitchat/greet&#x27;], this
will only return [&#x27;utter_chitchat/greet&#x27;] as only that will need a
response.

#### check\_missing\_responses

```python
 | check_missing_responses() -> None
```

Warn user of utterance names which have no specified response.

#### is\_empty

```python
 | is_empty() -> bool
```

Check whether the domain is empty.

#### is\_domain\_file

```python
 | @staticmethod
 | is_domain_file(filename: Union[Text, Path]) -> bool
```

Checks whether the given file path is a Rasa domain file.

**Arguments**:

- `filename` - Path of the file which should be checked.
  

**Returns**:

  `True` if it&#x27;s a domain file, otherwise `False`.
  

**Raises**:

- `YamlException` - if the file seems to be a YAML file (extension) but
  can not be read / parsed.

#### required\_slots\_for\_form

```python
 | required_slots_for_form(form_name: Text) -> List[Text]
```

Retrieve the list of required slot names for a form defined in the domain.

**Arguments**:

- `form_name` - The name of the form.
  

**Returns**:

  The list of slot names or an empty list if no form was found.

#### count\_slot\_mapping\_statistics

```python
 | count_slot_mapping_statistics() -> Tuple[int, int, int]
```

Counts the total number of slot mappings and custom slot mappings.

**Returns**:

  A triple of integers where the first entry is the total number of mappings,
  the second entry is the total number of custom mappings, and the third entry
  is the total number of mappings which have conditions attached.

#### \_\_repr\_\_

```python
 | __repr__() -> Text
```

Returns text representation of object.

#### warn\_about\_duplicates\_found\_during\_domain\_merging

```python
warn_about_duplicates_found_during_domain_merging(duplicates: Dict[Text, List[Text]]) -> None
```

Emits warning about found duplicates while loading multiple domain paths.

