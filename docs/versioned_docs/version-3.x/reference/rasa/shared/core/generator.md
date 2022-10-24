---
sidebar_label: rasa.shared.core.generator
title: rasa.shared.core.generator
---
## TrackerWithCachedStates Objects

```python
class TrackerWithCachedStates(DialogueStateTracker)
```

A tracker wrapper that caches the state creation of the tracker.

#### \_\_init\_\_

```python
def __init__(sender_id: Text,
             slots: Optional[Iterable[Slot]],
             max_event_history: Optional[int] = None,
             domain: Optional[Domain] = None,
             is_augmented: bool = False,
             is_rule_tracker: bool = False) -> None
```

Initializes a tracker with cached states.

#### from\_events

```python
@classmethod
def from_events(cls,
                sender_id: Text,
                evts: List[Event],
                slots: Optional[Iterable[Slot]] = None,
                max_event_history: Optional[int] = None,
                sender_source: Optional[Text] = None,
                domain: Optional[Domain] = None,
                is_rule_tracker: bool = False) -> "TrackerWithCachedStates"
```

Initializes a tracker with given events.

#### past\_states\_for\_hashing

```python
def past_states_for_hashing(domain: Domain,
                            omit_unset_slots: bool = False
                            ) -> Deque[FrozenState]
```

Generates and caches the past states of this tracker based on the history.

**Arguments**:

- `domain` - a :class:`rasa.shared.core.domain.Domain`
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A list of states

#### past\_states

```python
def past_states(
        domain: Domain,
        omit_unset_slots: bool = False,
        ignore_rule_only_turns: bool = False,
        rule_only_data: Optional[Dict[Text, Any]] = None) -> List[State]
```

Generates the past states of this tracker based on the history.

**Arguments**:

- `domain` - The Domain.
- `omit_unset_slots` - If `True` do not include the initial values of slots.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  a list of states

#### clear\_states

```python
def clear_states() -> None
```

Reset the states.

#### init\_copy

```python
def init_copy() -> "TrackerWithCachedStates"
```

Create a new state tracker with the same initial values.

#### copy

```python
def copy(sender_id: Text = "",
         sender_source: Text = "") -> "TrackerWithCachedStates"
```

Creates a duplicate of this tracker.

A new tracker will be created and all events
will be replayed.

#### update

```python
def update(event: Event, domain: Optional[Domain] = None) -> None
```

Modify the state of the tracker according to an ``Event``.

## TrainingDataGenerator Objects

```python
class TrainingDataGenerator()
```

Generates trackers from training data.

#### \_\_init\_\_

```python
def __init__(story_graph: StoryGraph,
             domain: Domain,
             remove_duplicates: bool = True,
             unique_last_num_states: Optional[int] = None,
             augmentation_factor: int = 50,
             tracker_limit: Optional[int] = None,
             use_story_concatenation: bool = True,
             debug_plots: bool = False)
```

Given a set of story parts, generates all stories that are possible.

The different story parts can end and start with checkpoints
and this generator will match start and end checkpoints to
connect complete stories. Afterwards, duplicate stories will be
removed and the data is augmented (if augmentation is enabled).

#### generate

```python
def generate() -> List[TrackerWithCachedStates]
```

Generate trackers from stories and rules.

**Returns**:

  The generated trackers.

#### generate\_story\_trackers

```python
def generate_story_trackers() -> List[TrackerWithCachedStates]
```

Generate trackers from stories (exclude rule trackers).

**Returns**:

  The generated story trackers.

