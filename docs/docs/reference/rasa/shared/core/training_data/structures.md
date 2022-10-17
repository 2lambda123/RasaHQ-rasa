---
sidebar_label: rasa.shared.core.training_data.structures
title: rasa.shared.core.training_data.structures
---
## EventTypeError Objects

```python
class EventTypeError(RasaCoreException,  ValueError)
```

Represents an error caused by a Rasa Core event not being of the expected
type.

## Checkpoint Objects

```python
class Checkpoint()
```

Represents places where trackers split.

This currently happens if
- users place manual checkpoints in their stories
- have `or` statements for intents in their stories.

#### \_\_init\_\_

```python
 | __init__(name: Text, conditions: Optional[Dict[Text, Any]] = None) -> None
```

Creates `Checkpoint`.

**Arguments**:

- `name` - Name of the checkpoint.
- `conditions` - Slot conditions for this checkpoint.

#### filter\_trackers

```python
 | filter_trackers(trackers: List[DialogueStateTracker]) -> List[DialogueStateTracker]
```

Filters out all trackers that do not satisfy the conditions.

## StoryStep Objects

```python
class StoryStep()
```

A StoryStep is a section of a story block between two checkpoints.

NOTE: Checkpoints are not only limited to those manually written
in the story file, but are also implicitly created at points where
multiple intents are separated in one line by chaining them with &quot;OR&quot;s.

#### \_\_init\_\_

```python
 | __init__(block_name: Text, start_checkpoints: Optional[List[Checkpoint]] = None, end_checkpoints: Optional[List[Checkpoint]] = None, events: Optional[List[Union[Event, List[Event]]]] = None, source_name: Optional[Text] = None) -> None
```

Initialise `StoryStep` default attributes.

#### as\_story\_string

```python
 | as_story_string(flat: bool = False, e2e: bool = False) -> Text
```

Returns a story as a string.

#### is\_action\_unlikely\_intent

```python
 | @staticmethod
 | is_action_unlikely_intent(event: Event) -> bool
```

Checks if the executed action is a `action_unlikely_intent`.

#### is\_action\_session\_start

```python
 | @staticmethod
 | is_action_session_start(event: Event) -> bool
```

Checks if the executed action is a `action_session_start`.

#### explicit\_events

```python
 | explicit_events(domain: Domain, should_append_final_listen: bool = True) -> List[Event]
```

Returns events contained in the story step including implicit events.

Not all events are always listed in the story dsl. This
includes listen actions as well as implicitly
set slots. This functions makes these events explicit and
returns them with the rest of the steps events.

## RuleStep Objects

```python
class RuleStep(StoryStep)
```

A Special type of StoryStep representing a Rule.

#### get\_rules\_condition

```python
 | get_rules_condition() -> List[Union[Event, List[Event]]]
```

Returns a list of events forming a condition of the Rule.

#### get\_rules\_events

```python
 | get_rules_events() -> List[Union[Event, List[Event]]]
```

Returns a list of events forming the Rule, that are not conditions.

#### add\_event\_as\_condition

```python
 | add_event_as_condition(event: Event) -> None
```

Adds event to the Rule as part of its condition.

**Arguments**:

- `event` - The event to be added.

## Story Objects

```python
class Story()
```

#### from\_events

```python
 | @staticmethod
 | from_events(events: List[Event], story_name: Optional[Text] = None) -> "Story"
```

Create a story from a list of events.

## StoryGraph Objects

```python
class StoryGraph()
```

Graph of the story-steps pooled from all stories in the training data.

#### \_\_hash\_\_

```python
 | __hash__() -> int
```

Return hash for the story step.

**Returns**:

  Hash of the story step.

#### fingerprint

```python
 | fingerprint() -> Text
```

Returns a unique hash for the stories which is stable across python runs.

**Returns**:

  fingerprint of the stories

#### ordered\_steps

```python
 | ordered_steps() -> List[StoryStep]
```

Returns the story steps ordered by topological order of the DAG.

#### cyclic\_edges

```python
 | cyclic_edges() -> List[Tuple[Optional[StoryStep], Optional[StoryStep]]]
```

Returns the story steps ordered by topological order of the DAG.

#### merge

```python
 | merge(other: Optional["StoryGraph"]) -> "StoryGraph"
```

Merge two StoryGraph together.

#### overlapping\_checkpoint\_names

```python
 | @staticmethod
 | overlapping_checkpoint_names(cps: List[Checkpoint], other_cps: List[Checkpoint]) -> Set[Text]
```

Find overlapping checkpoints names.

#### with\_cycles\_removed

```python
 | with_cycles_removed() -> "StoryGraph"
```

Create a graph with the cyclic edges removed from this graph.

#### order\_steps

```python
 | @staticmethod
 | order_steps(story_steps: List[StoryStep]) -> Tuple[deque, List[Tuple[Text, Text]]]
```

Topological sort of the steps returning the ids of the steps.

#### topological\_sort

```python
 | @staticmethod
 | topological_sort(graph: Dict[Text, Set[Text]]) -> Tuple[deque, List[Tuple[Text, Text]]]
```

Creates a top sort of a directed graph. This is an unstable sorting!

The function returns the sorted nodes as well as the edges that need
to be removed from the graph to make it acyclic (and hence, sortable).

The graph should be represented as a dictionary, e.g.:

&gt;&gt;&gt; example_graph = {
...         &quot;a&quot;: set(&quot;b&quot;, &quot;c&quot;, &quot;d&quot;),
...         &quot;b&quot;: set(),
...         &quot;c&quot;: set(&quot;d&quot;),
...         &quot;d&quot;: set(),
...         &quot;e&quot;: set(&quot;f&quot;),
...         &quot;f&quot;: set()}
&gt;&gt;&gt; StoryGraph.topological_sort(example_graph)
(deque([u&#x27;e&#x27;, u&#x27;f&#x27;, u&#x27;a&#x27;, u&#x27;c&#x27;, u&#x27;d&#x27;, u&#x27;b&#x27;]), [])

#### is\_empty

```python
 | is_empty() -> bool
```

Checks if `StoryGraph` is empty.

#### \_\_repr\_\_

```python
 | __repr__() -> Text
```

Returns text representation of object.

#### generate\_id

```python
generate_id(prefix: Text = "", max_chars: Optional[int] = None) -> Text
```

Generate a random UUID.

**Arguments**:

- `prefix` - String to prefix the ID with.
- `max_chars` - Maximum number of characters.
  

**Returns**:

  Generated random UUID.

