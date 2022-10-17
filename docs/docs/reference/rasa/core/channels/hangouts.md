---
sidebar_label: rasa.core.channels.hangouts
title: rasa.core.channels.hangouts
---
## HangoutsOutput Objects

```python
class HangoutsOutput(OutputChannel)
```

A Hangouts communication channel.

#### name

```python
 | @classmethod
 | name(cls) -> Text
```

Return channel name.

#### \_\_init\_\_

```python
 | __init__() -> None
```

Starts messages as empty dictionary.

#### send\_custom\_json

```python
 | async send_custom_json(recipient_id: Text, json_message: Dict, **kwargs: Any) -> None
```

Custom json payload is simply forwarded to Google Hangouts without
any modifications. Use this for more complex cards, which can be created
in actions.py.

## HangoutsInput Objects

```python
class HangoutsInput(InputChannel)
```

Channel that uses Google Hangouts Chat API to communicate.

#### name

```python
 | @classmethod
 | name(cls) -> Text
```

Returns channel name.

#### blueprint

```python
 | blueprint(on_new_message: Callable[[UserMessage], Awaitable[None]]) -> Blueprint
```

API configuration for the channel webhook.

