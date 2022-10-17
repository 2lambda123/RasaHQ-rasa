---
sidebar_label: rasa.engine.storage.local_model_storage
title: rasa.engine.storage.local_model_storage
---
## LocalModelStorage Objects

```python
class LocalModelStorage(ModelStorage)
```

Stores and provides output of `GraphComponents` on local disk.

#### \_\_init\_\_

```python
 | __init__(storage_path: Path) -> None
```

Creates storage (see parent class for full docstring).

#### create

```python
 | @classmethod
 | create(cls, storage_path: Path) -> ModelStorage
```

Creates a new instance (see parent class for full docstring).

#### from\_model\_archive

```python
 | @classmethod
 | from_model_archive(cls, storage_path: Path, model_archive_path: Union[Text, Path]) -> Tuple[LocalModelStorage, ModelMetadata]
```

Initializes storage from archive (see parent class for full docstring).

#### metadata\_from\_archive

```python
 | @classmethod
 | metadata_from_archive(cls, model_archive_path: Union[Text, Path]) -> ModelMetadata
```

Retrieves metadata from archive (see parent class for full docstring).

#### write\_to

```python
 | @contextmanager
 | write_to(resource: Resource) -> Generator[Path, None, None]
```

Persists data for a resource (see parent class for full docstring).

#### read\_from

```python
 | @contextmanager
 | read_from(resource: Resource) -> Generator[Path, None, None]
```

Provides the data of a `Resource` (see parent class for full docstring).

#### create\_model\_package

```python
 | create_model_package(model_archive_path: Union[Text, Path], model_configuration: GraphModelConfiguration, domain: Domain) -> ModelMetadata
```

Creates model package (see parent class for full docstring).

