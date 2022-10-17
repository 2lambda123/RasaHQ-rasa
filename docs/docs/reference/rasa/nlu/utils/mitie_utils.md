---
sidebar_label: rasa.nlu.utils.mitie_utils
title: rasa.nlu.utils.mitie_utils
---
## MitieModel Objects

```python
class MitieModel()
```

Wraps `MitieNLP` output to make it fingerprintable.

#### \_\_init\_\_

```python
 | __init__(model_path: Path, word_feature_extractor: Optional["mitie.total_word_feature_extractor"] = None) -> None
```

Initializing MitieModel.

#### fingerprint

```python
 | fingerprint() -> Text
```

Fingerprints the model path.

Use a static fingerprint as we assume this only changes if the file path
changes and want to avoid investigating the model in greater detail for now.

**Returns**:

  Fingerprint for model.

## MitieNLP Objects

```python
@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.MODEL_LOADER, is_trainable=False
)
class MitieNLP(GraphComponent)
```

Component which provides the common configuration and loaded model to others.

This is used to avoid loading the Mitie model multiple times. Instead the Mitie
model is only loaded once and then shared by depending components.

#### get\_default\_config

```python
 | @staticmethod
 | get_default_config() -> Dict[Text, Any]
```

Returns default config (see parent class for full docstring).

#### \_\_init\_\_

```python
 | __init__(path_to_model_file: Path, extractor: Optional["mitie.total_word_feature_extractor"] = None) -> None
```

Constructs a new language model from the MITIE framework.

#### required\_packages

```python
 | @classmethod
 | required_packages(cls) -> List[Text]
```

Lists required dependencies (see parent class for full docstring).

#### create

```python
 | @classmethod
 | create(cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext) -> MitieNLP
```

Creates component (see parent class for full docstring).

#### provide

```python
 | provide() -> MitieModel
```

Provides loaded `MitieModel` and path during training and inference.

