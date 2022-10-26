---
sidebar_label: rasa.core.tracker_store
title: rasa.core.tracker_store
---
#### check\_if\_tracker\_store\_async

```python
def check_if_tracker_store_async(tracker_store: TrackerStore) -> bool
```

Evaluates if a tracker store object is async based on implementation of methods.

**Arguments**:

- `tracker_store`: tracker store object we&#x27;re evaluating

**Returns**:

if the tracker store correctly implements all async methods

## TrackerDeserialisationException Objects

```python
class TrackerDeserialisationException(RasaException)
```

Raised when an error is encountered while deserialising a tracker.

## SerializedTrackerRepresentation Objects

```python
class SerializedTrackerRepresentation(Generic[SerializationType])
```

Mixin class for specifying different serialization methods per tracker store.

#### serialise\_tracker

```python
@staticmethod
def serialise_tracker(tracker: DialogueStateTracker) -> SerializationType
```

Requires implementation to return representation of tracker.

## SerializedTrackerAsText Objects

```python
class SerializedTrackerAsText(SerializedTrackerRepresentation[Text])
```

Mixin class that returns the serialized tracker as string.

#### serialise\_tracker

```python
@staticmethod
def serialise_tracker(tracker: DialogueStateTracker) -> Text
```

Serializes the tracker, returns representation of the tracker.

## SerializedTrackerAsDict Objects

```python
class SerializedTrackerAsDict(SerializedTrackerRepresentation[Dict])
```

Mixin class that returns the serialized tracker as dictionary.

#### serialise\_tracker

```python
@staticmethod
def serialise_tracker(tracker: DialogueStateTracker) -> Dict
```

Serializes the tracker, returns representation of the tracker.

## TrackerStore Objects

```python
class TrackerStore()
```

Represents common behavior and interface for all `TrackerStore`s.

#### \_\_init\_\_

```python
def __init__(domain: Optional[Domain],
             event_broker: Optional[EventBroker] = None,
             **kwargs: Dict[Text, Any]) -> None
```

Create a TrackerStore.

**Arguments**:

- `domain` - The `Domain` to initialize the `DialogueStateTracker`.
- `event_broker` - An event broker to publish any new events to another
  destination.
- `kwargs` - Additional kwargs.

#### create

```python
@staticmethod
def create(obj: Union[TrackerStore, EndpointConfig, None],
           domain: Optional[Domain] = None,
           event_broker: Optional[EventBroker] = None) -> TrackerStore
```

Factory to create a tracker store.

#### get\_or\_create\_tracker

```python
async def get_or_create_tracker(
        sender_id: Text,
        max_event_history: Optional[int] = None,
        append_action_listen: bool = True) -> "DialogueStateTracker"
```

Returns tracker or creates one if the retrieval returns None.

**Arguments**:

- `sender_id` - Conversation ID associated with the requested tracker.
- `max_event_history` - Value to update the tracker store&#x27;s max event history to.
- `append_action_listen` - Whether or not to append an initial `action_listen`.

#### init\_tracker

```python
def init_tracker(sender_id: Text) -> "DialogueStateTracker"
```

Returns a Dialogue State Tracker.

#### create\_tracker

```python
async def create_tracker(
        sender_id: Text,
        append_action_listen: bool = True) -> DialogueStateTracker
```

Creates a new tracker for `sender_id`.

The tracker begins with a `SessionStarted` event and is initially listening.

**Arguments**:

- `sender_id` - Conversation ID associated with the tracker.
- `append_action_listen` - Whether or not to append an initial `action_listen`.
  

**Returns**:

  The newly created tracker for `sender_id`.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Save method that will be overridden by specific tracker.

#### exists

```python
async def exists(conversation_id: Text) -> bool
```

Checks if tracker exists for the specified ID.

This method may be overridden by the specific tracker store for
faster implementations.

**Arguments**:

- `conversation_id` - Conversation ID to check if the tracker exists.
  

**Returns**:

  `True` if the tracker exists, `False` otherwise.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Retrieves tracker for the latest conversation session.

This method will be overridden by the specific tracker store.

**Arguments**:

- `sender_id` - Conversation ID to fetch the tracker for.
  

**Returns**:

  Tracker containing events from the latest conversation sessions.

#### retrieve\_full\_tracker

```python
async def retrieve_full_tracker(
        conversation_id: Text) -> Optional[DialogueStateTracker]
```

Retrieve method for fetching all tracker events across conversation sessions\
that may be overridden by specific tracker.

The default implementation uses `self.retrieve()`.

**Arguments**:

- `conversation_id` - The conversation ID to retrieve the tracker for.
  

**Returns**:

  The fetch tracker containing all events across session starts.

#### stream\_events

```python
async def stream_events(tracker: DialogueStateTracker) -> None
```

Streams events to a message broker.

#### number\_of\_existing\_events

```python
async def number_of_existing_events(sender_id: Text) -> int
```

Return number of stored events for a given sender id.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns the set of values for the tracker store&#x27;s primary key.

#### deserialise\_tracker

```python
def deserialise_tracker(
        sender_id: Text,
        serialised_tracker: Union[Text,
                                  bytes]) -> Optional[DialogueStateTracker]
```

Deserializes the tracker and returns it.

#### domain

```python
@property
def domain() -> Domain
```

Returns the domain of the tracker store.

## InMemoryTrackerStore Objects

```python
class InMemoryTrackerStore(TrackerStore, SerializedTrackerAsText)
```

Stores conversation history in memory.

#### \_\_init\_\_

```python
def __init__(domain: Domain,
             event_broker: Optional[EventBroker] = None,
             **kwargs: Dict[Text, Any]) -> None
```

Initializes the tracker store.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Updates and saves the current conversation state.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Returns tracker matching sender_id.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns sender_ids of the Tracker Store in memory.

## RedisTrackerStore Objects

```python
class RedisTrackerStore(TrackerStore, SerializedTrackerAsText)
```

Stores conversation history in Redis.

#### \_\_init\_\_

```python
def __init__(domain: Domain,
             host: Text = "localhost",
             port: int = 6379,
             db: int = 0,
             password: Optional[Text] = None,
             event_broker: Optional[EventBroker] = None,
             record_exp: Optional[float] = None,
             key_prefix: Optional[Text] = None,
             use_ssl: bool = False,
             ssl_keyfile: Optional[Text] = None,
             ssl_certfile: Optional[Text] = None,
             ssl_ca_certs: Optional[Text] = None,
             **kwargs: Dict[Text, Any]) -> None
```

Initializes the tracker store.

#### save

```python
async def save(tracker: DialogueStateTracker,
               timeout: Optional[float] = None) -> None
```

Saves the current conversation state.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Retrieves tracker for the latest conversation session.

The Redis key is formed by appending a prefix to sender_id.

**Arguments**:

- `sender_id` - Conversation ID to fetch the tracker for.
  

**Returns**:

  Tracker containing events from the latest conversation sessions.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns keys of the Redis Tracker Store.

## DynamoTrackerStore Objects

```python
class DynamoTrackerStore(TrackerStore, SerializedTrackerAsDict)
```

Stores conversation history in DynamoDB.

#### \_\_init\_\_

```python
def __init__(domain: Domain,
             table_name: Text = "states",
             region: Text = "us-east-1",
             event_broker: Optional[EndpointConfig] = None,
             **kwargs: Dict[Text, Any]) -> None
```

Initialize `DynamoTrackerStore`.

**Arguments**:

- `domain` - Domain associated with this tracker store.
- `table_name` - The name of the DynamoDB table, does not need to be present a
  priori.
- `region` - The name of the region associated with the client.
  A client is associated with a single region.
- `event_broker` - An event broker used to publish events.
- `kwargs` - Additional kwargs.

#### get\_or\_create\_table

```python
def get_or_create_table(
        table_name: Text) -> "boto3.resources.factory.dynamodb.Table"
```

Returns table or creates one if the table name is not in the table list.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Saves the current conversation state.

#### serialise\_tracker

```python
@staticmethod
def serialise_tracker(tracker: "DialogueStateTracker") -> Dict
```

Serializes the tracker, returns object with decimal types.

DynamoDB cannot store `float`s, so we&#x27;ll convert them to `Decimal`s.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Retrieve dialogues for a sender_id in reverse-chronological order.

Based on the session_date sort key.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns sender_ids of the `DynamoTrackerStore`.

## MongoTrackerStore Objects

```python
class MongoTrackerStore(TrackerStore, SerializedTrackerAsText)
```

Stores conversation history in Mongo.

Property methods:
    conversations: returns the current conversation

#### conversations

```python
@property
def conversations() -> Collection
```

Returns the current conversation.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Saves the current conversation state.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Retrieves tracker for the latest conversation session.

#### retrieve\_full\_tracker

```python
async def retrieve_full_tracker(
        conversation_id: Text) -> Optional[DialogueStateTracker]
```

Fetching all tracker events across conversation sessions.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns sender_ids of the Mongo Tracker Store.

#### is\_postgresql\_url

```python
def is_postgresql_url(url: Union[Text, "URL"]) -> bool
```

Determine whether `url` configures a PostgreSQL connection.

**Arguments**:

- `url` - SQL connection URL.
  

**Returns**:

  `True` if `url` is a PostgreSQL connection URL.

#### create\_engine\_kwargs

```python
def create_engine_kwargs(url: Union[Text, "URL"]) -> Dict[Text, Any]
```

Get `sqlalchemy.create_engine()` kwargs.

**Arguments**:

- `url` - SQL connection URL.
  

**Returns**:

  kwargs to be passed into `sqlalchemy.create_engine()`.

#### ensure\_schema\_exists

```python
def ensure_schema_exists(session: "Session") -> None
```

Ensure that the requested PostgreSQL schema exists in the database.

**Arguments**:

- `session` - Session used to inspect the database.
  

**Raises**:

  `ValueError` if the requested schema does not exist.

#### validate\_port

```python
def validate_port(port: Any) -> Optional[int]
```

Ensure that port can be converted to integer.

**Raises**:

  RasaException if port cannot be cast to integer.

## SQLTrackerStore Objects

```python
class SQLTrackerStore(TrackerStore, SerializedTrackerAsText)
```

Store which can save and retrieve trackers from an SQL database.

## SQLEvent Objects

```python
class SQLEvent(Base)
```

Represents an event in the SQL Tracker Store.

#### get\_db\_url

```python
@staticmethod
def get_db_url(dialect: Text = "sqlite",
               host: Optional[Text] = None,
               port: Optional[int] = None,
               db: Text = "rasa.db",
               username: Text = None,
               password: Text = None,
               login_db: Optional[Text] = None,
               query: Optional[Dict] = None) -> Union[Text, "URL"]
```

Build an SQLAlchemy `URL` object representing the parameters needed
to connect to an SQL database.

**Arguments**:

- `dialect` - SQL database type.
- `host` - Database network host.
- `port` - Database network port.
- `db` - Database name.
- `username` - User name to use when connecting to the database.
- `password` - Password for database user.
- `login_db` - Alternative database name to which initially connect, and create
  the database specified by `db` (PostgreSQL only).
- `query` - Dictionary of options to be passed to the dialect and/or the
  DBAPI upon connect.
  

**Returns**:

  URL ready to be used with an SQLAlchemy `Engine` object.

#### session\_scope

```python
@contextlib.contextmanager
def session_scope() -> Generator["Session", None, None]
```

Provide a transactional scope around a series of operations.

#### keys

```python
async def keys() -> Iterable[Text]
```

Returns sender_ids of the SQLTrackerStore.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Retrieves tracker for the latest conversation session.

#### retrieve\_full\_tracker

```python
async def retrieve_full_tracker(
        conversation_id: Text) -> Optional[DialogueStateTracker]
```

Fetching all tracker events across conversation sessions.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Update database with events from the current conversation.

## FailSafeTrackerStore Objects

```python
class FailSafeTrackerStore(TrackerStore)
```

Tracker store wrapper.

Allows a fallback to a different tracker store in case of errors.

#### \_\_init\_\_

```python
def __init__(tracker_store: TrackerStore,
             on_tracker_store_error: Optional[Callable[[Exception],
                                                       None]] = None,
             fallback_tracker_store: Optional[TrackerStore] = None) -> None
```

Create a `FailSafeTrackerStore`.

**Arguments**:

- `tracker_store` - Primary tracker store.
- `on_tracker_store_error` - Callback which is called when there is an error
  in the primary tracker store.

#### domain

```python
@property
def domain() -> Domain
```

Returns the domain of the primary tracker store.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Calls `retrieve` method of primary tracker store.

#### keys

```python
async def keys() -> Iterable[Text]
```

Calls `keys` method of primary tracker store.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Calls `save` method of primary tracker store.

## AwaitableTrackerStore Objects

```python
class AwaitableTrackerStore(TrackerStore)
```

Wraps a tracker store so it can be implemented with async overrides.

#### \_\_init\_\_

```python
def __init__(tracker_store: TrackerStore) -> None
```

Create a `AwaitableTrackerStore`.

**Arguments**:

- `tracker_store` - the wrapped tracker store.

#### domain

```python
@property
def domain() -> Domain
```

Returns the domain of the primary tracker store.

#### domain

```python
@domain.setter
def domain(domain: Optional[Domain]) -> None
```

Setter method to modify the wrapped tracker store&#x27;s domain field.

#### create

```python
@staticmethod
def create(obj: Union[TrackerStore, EndpointConfig, None],
           domain: Optional[Domain] = None,
           event_broker: Optional[EventBroker] = None) -> TrackerStore
```

Wrapper to call `create` method of primary tracker store.

#### retrieve

```python
async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]
```

Wrapper to call `retrieve` method of primary tracker store.

#### keys

```python
async def keys() -> Iterable[Text]
```

Wrapper to call `keys` method of primary tracker store.

#### save

```python
async def save(tracker: DialogueStateTracker) -> None
```

Wrapper to call `save` method of primary tracker store.

#### retrieve\_full\_tracker

```python
async def retrieve_full_tracker(
        conversation_id: Text) -> Optional[DialogueStateTracker]
```

Wrapper to call `retrieve_full_tracker` method of primary tracker store.

