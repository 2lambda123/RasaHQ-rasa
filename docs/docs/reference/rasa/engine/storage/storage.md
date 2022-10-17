---
sidebar_label: rasa.engine.storage.storage
title: rasa.engine.storage.storage
---
## ModelStorage Objects

```python
class ModelStorage(abc.ABC)
```

Serves as storage backend for `GraphComponents` which need persistence.

#### create

```python
 | @classmethod
 | @abc.abstractmethod
 | create(cls, storage_path: Path) -> ModelStorage
```

Creates the storage.

**Arguments**:

- `storage_path` - Directory which will contain the persisted graph components.

#### from\_model\_archive

```python
 | @classmethod
 | @abc.abstractmethod
 | from_model_archive(cls, storage_path: Path, model_archive_path: Union[Text, Path]) -> Tuple[ModelStorage, ModelMetadata]
```

Unpacks a model archive and initializes a `ModelStorage`.

**Arguments**:

- `storage_path` - Directory which will contain the persisted graph components.
- `model_archive_path` - The path to the model archive.
  

**Returns**:

  Initialized model storage, and metadata about the model.
  

**Raises**:

  `UnsupportedModelError` if the loaded meta data indicates that the model
  has been created with an outdated Rasa version.

#### metadata\_from\_archive

```python
 | @classmethod
 | metadata_from_archive(cls, model_archive_path: Union[Text, Path]) -> ModelMetadata
```

Retrieves metadata from archive.

**Arguments**:

- `model_archive_path` - The path to the model archive.
  

**Returns**:

  Metadata about the model.
  

**Raises**:

  `UnsupportedModelError` if the loaded meta data indicates that the model
  has been created with an outdated Rasa version.

#### write\_to

```python
 | @contextmanager
 | @abc.abstractmethod
 | write_to(resource: Resource) -> Generator[Path, None, None]
```

Persists data for a given resource.

This `Resource` can then be accessed in dependent graph nodes via
`model_storage.read_from`.

**Arguments**:

- `resource` - The resource which should be persisted.
  

**Returns**:

  A directory which can be used to persist data for the given `Resource`.

#### read\_from

```python
 | @contextmanager
 | @abc.abstractmethod
 | read_from(resource: Resource) -> Generator[Path, None, None]
```

Provides the data of a persisted `Resource`.

**Arguments**:

- `resource` - The `Resource` whose persisted should be accessed.
  

**Returns**:

  A directory containing the data of the persisted `Resource`.
  

**Raises**:

- `ValueError` - In case no persisted data for the given `Resource` exists.

#### create\_model\_package

```python
 | create_model_package(model_archive_path: Union[Text, Path], model_configuration: GraphModelConfiguration, domain: Domain) -> ModelMetadata
```

Creates a model archive containing all data to load and run the model.

**Arguments**:

- `model_archive_path` - The path to the archive which should be created.
- `model_configuration` - The model configuration (schemas, language, etc.)
- `domain` - The `Domain` which was used to train the model.
  

**Returns**:

  The model metadata.

## ModelMetadata Objects

```python
@dataclass()
class ModelMetadata()
```

Describes a trained model.

#### \_\_post\_init\_\_

```python
 | __post_init__() -> None
```

Raises an exception when the meta data indicates an unsupported version.

**Raises**:

  `UnsupportedModelException` if the `rasa_open_source_version` is lower
  than the minimum compatible version

#### as\_dict

```python
 | as_dict() -> Dict[Text, Any]
```

Returns serializable version of the `ModelMetadata`.

#### from\_dict

```python
 | @classmethod
 | from_dict(cls, serialized: Dict[Text, Any]) -> ModelMetadata
```

Loads `ModelMetadata` which has been serialized using `metadata.as_dict()`.

**Arguments**:

- `serialized` - Serialized `ModelMetadata` (e.g. read from disk).
  

**Returns**:

  Instantiated `ModelMetadata`.

