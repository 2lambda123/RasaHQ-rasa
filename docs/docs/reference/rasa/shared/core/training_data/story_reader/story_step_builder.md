---
sidebar_label: rasa.shared.core.training_data.story_reader.story_step_builder
title: rasa.shared.core.training_data.story_reader.story_step_builder
---
## StoryStepBuilder Objects

```python
class StoryStepBuilder()
```

#### add\_checkpoint

```python
def add_checkpoint(name: Text, conditions: Optional[Dict[Text, Any]]) -> None
```

Add a checkpoint to story steps.

#### add\_user\_messages

```python
def add_user_messages(messages: List[UserUttered]) -> None
```

Adds next story steps with the user&#x27;s utterances.

**Arguments**:

- `messages` - User utterances.

#### add\_events

```python
def add_events(events: List[Event]) -> None
```

Adds next story steps with the specified list of events.

**Arguments**:

- `events` - Events that need to be added.

