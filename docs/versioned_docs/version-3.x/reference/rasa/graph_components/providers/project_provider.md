---
sidebar_label: rasa.graph_components.providers.project_provider
title: rasa.graph_components.providers.project_provider
---
## ProjectProvider Objects

```python
class ProjectProvider(GraphComponent)
```

Provides domain and training data during training and inference time.

#### get\_default\_config

```python
 | @staticmethod
 | get_default_config() -> Dict[Text, Any]
```

Default config for ProjectProvider.

#### \_\_init\_\_

```python
 | __init__(config: Dict[Text, Any]) -> None
```

Initializes the ProjectProvider.

#### create

```python
 | @classmethod
 | create(cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext) -> ProjectProvider
```

Creates component (see parent class for full docstring).

#### provide

```python
 | provide() -> TrainingDataImporter
```

Provides the TrainingDataImporter.

