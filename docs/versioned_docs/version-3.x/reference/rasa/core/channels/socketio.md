---
sidebar_label: rasa.core.channels.socketio
title: rasa.core.channels.socketio
---
## SocketBlueprint Objects

```python
class SocketBlueprint(Blueprint)
```

#### \_\_init\_\_

```python
def __init__(sio: AsyncServer, socketio_path: Text, *args: Any,
             **kwargs: Any) -> None
```

Creates a :class:`sanic.Blueprint` for routing socketio connenctions.

**Arguments**:

- `sio`: Instance of :class:`socketio.AsyncServer` class
- `socketio_path`: string indicating the route to accept requests on.

#### register

```python
def register(app: Sanic, options: Dict[Text, Any]) -> None
```

Attach the Socket.IO webserver to the given Sanic instance.

**Arguments**:

- `app`: Instance of :class:`sanic.app.Sanic` class
- `options`: Options to be used while registering the
blueprint into the app.

## SocketIOOutput Objects

```python
class SocketIOOutput(OutputChannel)
```

#### send\_text\_message

```python
async def send_text_message(recipient_id: Text, text: Text,
                            **kwargs: Any) -> None
```

Send a message through this channel.

#### send\_image\_url

```python
async def send_image_url(recipient_id: Text, image: Text,
                         **kwargs: Any) -> None
```

Sends an image to the output

#### send\_text\_with\_buttons

```python
async def send_text_with_buttons(recipient_id: Text, text: Text,
                                 buttons: List[Dict[Text, Any]],
                                 **kwargs: Any) -> None
```

Sends buttons to the output.

#### send\_elements

```python
async def send_elements(recipient_id: Text, elements: Iterable[Dict[Text,
                                                                    Any]],
                        **kwargs: Any) -> None
```

Sends elements to the output.

#### send\_custom\_json

```python
async def send_custom_json(recipient_id: Text, json_message: Dict[Text, Any],
                           **kwargs: Any) -> None
```

Sends custom json to the output

#### send\_attachment

```python
async def send_attachment(recipient_id: Text, attachment: Dict[Text, Any],
                          **kwargs: Any) -> None
```

Sends an attachment to the user.

## SocketIOInput Objects

```python
class SocketIOInput(InputChannel)
```

A socket.io input channel.

#### \_\_init\_\_

```python
def __init__(user_message_evt: Text = "user_uttered",
             bot_message_evt: Text = "bot_uttered",
             namespace: Optional[Text] = None,
             session_persistence: bool = False,
             socketio_path: Optional[Text] = "/socket.io",
             jwt_key: Optional[Text] = None,
             jwt_method: Optional[Text] = "HS256")
```

Creates a ``SocketIOInput`` object.

#### get\_output\_channel

```python
def get_output_channel() -> Optional["OutputChannel"]
```

Creates socket.io output channel object.

#### blueprint

```python
def blueprint(
        on_new_message: Callable[[UserMessage], Awaitable[Any]]) -> Blueprint
```

Defines a Sanic blueprint.

