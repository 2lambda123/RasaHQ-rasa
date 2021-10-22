from typing import Type

import pytest

from rasa.shared.core.events import SlotSet, ActionExecuted, UserUttered
from rasa.core.evaluation.markers import (
    ActionExecutedMarker,
    AndMarker,
    AtomicMarker,
    IntentDetectedMarker,
    Marker,
    NotAnyMarker,
    OrMarker,
    SequenceMarker,
    SlotSetMarker,
)
from rasa.shared.nlu.constants import INTENT_NAME_KEY


EVENT_MARKERS = [ActionExecutedMarker, SlotSetMarker, IntentDetectedMarker]
COMPOUND_MARKERS = [AndMarker, OrMarker, NotAnyMarker]


def test_marker_from_config():

    config = [
        {
            "marker_1": {
                "and": [
                    {"slot_set": ["s1"]},
                    {"or": [{"intent_detected": ["4"]}, {"intent_detected": ["6"]},]},
                ]
            }
        }
    ]

    marker = Marker.from_config(config)

    assert marker.name == "marker_1"
    assert isinstance(marker, AndMarker)
    assert isinstance(marker.markers[0], SlotSetMarker)
    assert isinstance(marker.markers[1], OrMarker)
    for sub_marker in marker.markers[1].markers:
        assert isinstance(sub_marker, AtomicMarker)


@pytest.mark.parametrize("atomic_marker_type", EVENT_MARKERS)
def test_atomic_marker_track(atomic_marker_type: Type[AtomicMarker]):
    """Each marker applies an exact number of times (slots are immediately un-set)."""

    marker = atomic_marker_type(text="same-text", name="marker_name")

    events = [
        UserUttered(intent={"name": "1"}),
        UserUttered(intent={"name": "same-text"}),
        SlotSet("same-text", value="any"),
        SlotSet("same-text", value=None),
        ActionExecuted(action_name="same-text"),
    ]

    num_applies = 3
    events = events * num_applies

    for event in events:
        marker.track(event)

    assert len(marker.history) == len(events)
    assert sum(marker.history) == num_applies


@pytest.mark.parametrize("atomic_marker_type", EVENT_MARKERS)
def test_atomic_marker_evaluate_events(atomic_marker_type: Type[AtomicMarker]):
    """Each marker applies an exact number of times (slots are immediately un-set)."""

    events = [
        UserUttered(intent={INTENT_NAME_KEY: "1"}),
        UserUttered(intent={INTENT_NAME_KEY: "same-text"}),
        SlotSet("same-text", value="any"),
        SlotSet("same-text", value=None),
        ActionExecuted(action_name="same-text"),
    ]

    num_applies = 3
    events = events * num_applies

    marker = atomic_marker_type(text="same-text", name="marker_name")
    evaluation = marker.evaluate_events(events)

    assert "marker_name" in evaluation
    if atomic_marker_type == IntentDetectedMarker:
        expected = (1, 3, 5)
    else:
        expected = (2, 4, 6)
    assert evaluation["marker_name"]["preceeding_user_turns"] == expected


def test_compound_marker_or_track():

    sub_markers = [IntentDetectedMarker("1"), IntentDetectedMarker("2")]
    marker = OrMarker(sub_markers, name="marker_name")

    marker.track(UserUttered(intent={INTENT_NAME_KEY: "1"}))
    marker.track(UserUttered(intent={INTENT_NAME_KEY: "unknown"}))
    marker.track(UserUttered(intent={INTENT_NAME_KEY: "2"}))
    marker.track(UserUttered(intent={INTENT_NAME_KEY: "unknown"}))

    assert marker.history == [True, False, True, False]


def test_compound_marker_and_track():

    events_expected = [
        (UserUttered(intent={INTENT_NAME_KEY: "1"}), False),
        (SlotSet("2", value="bla"), False),
        (UserUttered(intent={INTENT_NAME_KEY: "1"}), True),
        (SlotSet("2", value=None), False),
        (UserUttered(intent={INTENT_NAME_KEY: "1"}), False),
        (SlotSet("2", value="bla"), False),
        (UserUttered(intent={INTENT_NAME_KEY: "2"}), False),
    ]
    events, expected = zip(*events_expected)

    sub_markers = [IntentDetectedMarker("1"), SlotSetMarker("2")]
    marker = AndMarker(sub_markers, name="marker_name")
    for event in events:
        marker.track(event)

    assert marker.history == list(expected)


def test_compound_marker_seq_track():

    events_expected = [
        (UserUttered(intent={INTENT_NAME_KEY: "1"}), False),
        (UserUttered(intent={INTENT_NAME_KEY: "2"}), True),
        (UserUttered(intent={INTENT_NAME_KEY: "3"}), False),
        (UserUttered(intent={INTENT_NAME_KEY: "1"}), False),
        (UserUttered(intent={INTENT_NAME_KEY: "2"}), True),
    ]
    events, expected = zip(*events_expected)

    sub_markers = [IntentDetectedMarker("1"), IntentDetectedMarker("2")]
    marker = SequenceMarker(sub_markers, name="marker_name")
    for event in events:
        marker.track(event)

    assert marker.history == list(expected)


def test_compound_marker_nested_track():

    events = [
        UserUttered(intent={"name": "1"}),
        UserUttered(intent={"name": "2"}),
        UserUttered(intent={"name": "3"}),
        SlotSet("s1", value="any"),
        UserUttered(intent={"name": "4"}),
        UserUttered(intent={"name": "5"}),
        UserUttered(intent={"name": "6"}),
    ]

    marker = AndMarker(
        markers=[
            SlotSetMarker("s1"),
            OrMarker([IntentDetectedMarker("4"), IntentDetectedMarker("6"),]),
        ],
        name="marker_name",
    )

    evaluation = marker.evaluate_events(events)

    assert evaluation["marker_name"]["preceeding_user_turns"] == (3, 5)
