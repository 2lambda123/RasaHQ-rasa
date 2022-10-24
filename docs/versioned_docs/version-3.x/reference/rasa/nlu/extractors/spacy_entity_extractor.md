---
sidebar_label: rasa.nlu.extractors.spacy_entity_extractor
title: rasa.nlu.extractors.spacy_entity_extractor
---
## SpacyEntityExtractor Objects

```python
@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR,
    is_trainable=False,
    model_from="SpacyNLP",
)
class SpacyEntityExtractor(GraphComponent, EntityExtractorMixin)
```

Entity extractor which uses SpaCy.

#### required\_components

```python
@classmethod
def required_components(cls) -> List[Type]
```

Components that should be included in the pipeline before this component.

#### get\_default\_config

```python
@staticmethod
def get_default_config() -> Dict[Text, Any]
```

The component&#x27;s default config (see parent class for full docstring).

#### \_\_init\_\_

```python
def __init__(config: Dict[Text, Any]) -> None
```

Initialize SpacyEntityExtractor.

#### create

```python
@classmethod
def create(cls, config: Dict[Text, Any], model_storage: ModelStorage,
           resource: Resource,
           execution_context: ExecutionContext) -> GraphComponent
```

Creates a new component (see parent class for full docstring).

#### required\_packages

```python
@staticmethod
def required_packages() -> List[Text]
```

Lists required dependencies (see parent class for full docstring).

#### process

```python
def process(messages: List[Message], model: SpacyModel) -> List[Message]
```

Extract entities using SpaCy.

**Arguments**:

- `messages` - List of messages to process.
- `model` - Container holding a loaded spacy nlp model.
  
- `Returns` - The processed messages.

