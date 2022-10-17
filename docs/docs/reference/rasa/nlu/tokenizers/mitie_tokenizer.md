---
sidebar_label: rasa.nlu.tokenizers.mitie_tokenizer
title: rasa.nlu.tokenizers.mitie_tokenizer
---
## MitieTokenizer Objects

```python
@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER, is_trainable=False
)
class MitieTokenizer(Tokenizer)
```

Tokenizes messages using the `mitie` library..

#### get\_default\_config

```python
 | @staticmethod
 | get_default_config() -> Dict[Text, Any]
```

Returns default config (see parent class for full docstring).

#### required\_packages

```python
 | @staticmethod
 | required_packages() -> List[Text]
```

Any extra python dependencies required for this component to run.

#### create

```python
 | @classmethod
 | create(cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext) -> MitieTokenizer
```

Creates a new component (see parent class for full docstring).

#### tokenize

```python
 | tokenize(message: Message, attribute: Text) -> List[Token]
```

Tokenizes the text of the provided attribute of the incoming message.

