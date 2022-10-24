---
sidebar_label: rasa.nlu.extractors.entity_synonyms
title: rasa.nlu.extractors.entity_synonyms
---
## EntitySynonymMapper Objects

```python
@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR, is_trainable=True
)
class EntitySynonymMapper(GraphComponent, EntityExtractorMixin)
```

Maps entities to their synonyms if they appear in the training data.

#### \_\_init\_\_

```python
def __init__(config: Optional[Dict[Text, Any]],
             model_storage: ModelStorage,
             resource: Resource,
             synonyms: Optional[Dict[Text, Any]] = None) -> None
```

Creates the mapper.

**Arguments**:

- `config` - The mapper&#x27;s config.
- `model_storage` - Storage which the component can use to persist and load
  itself.
- `resource` - Resource locator for this component which can be used to persist
  and load itself from the `model_storage`.
- `synonyms` - A dictionary of previously known synonyms.

#### create

```python
@classmethod
def create(cls,
           config: Dict[Text, Any],
           model_storage: ModelStorage,
           resource: Resource,
           execution_context: ExecutionContext,
           synonyms: Optional[Dict[Text, Any]] = None) -> EntitySynonymMapper
```

Creates component (see parent class for full docstring).

#### train

```python
def train(training_data: TrainingData) -> Resource
```

Trains the synonym lookup table.

#### process

```python
def process(messages: List[Message]) -> List[Message]
```

Modifies entities attached to message to resolve synonyms.

**Arguments**:

- `messages` - List containing the latest user message
  

**Returns**:

  List containing the latest user message with entities resolved to
  synonyms if there is a match.

#### load

```python
@classmethod
def load(cls, config: Dict[Text, Any], model_storage: ModelStorage,
         resource: Resource, execution_context: ExecutionContext,
         **kwargs: Any) -> EntitySynonymMapper
```

Loads trained component (see parent class for full docstring).

#### replace\_synonyms

```python
def replace_synonyms(entities: List[Dict[Text, Any]]) -> None
```

Replace any entities which match a synonym with the synonymous entity.

