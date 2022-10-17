---
sidebar_label: rasa.graph_components.providers.domain_provider
title: rasa.graph_components.providers.domain_provider
---
## DomainProvider Objects

```python
class DomainProvider(GraphComponent)
```

Provides domain during training and inference time.

#### \_\_init\_\_

```python
 | __init__(model_storage: ModelStorage, resource: Resource, domain: Optional[Domain] = None) -> None
```

Creates domain provider.

#### create

```python
 | @classmethod
 | create(cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext) -> DomainProvider
```

Creates component (see parent class for full docstring).

#### load

```python
 | @classmethod
 | load(cls, config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext, **kwargs: Any, ,) -> DomainProvider
```

Creates provider using a persisted version of itself.

#### provide\_train

```python
 | provide_train(importer: TrainingDataImporter) -> Domain
```

Provides domain from training data during training.

#### provide\_inference

```python
 | provide_inference() -> Domain
```

Provides the domain during inference.

