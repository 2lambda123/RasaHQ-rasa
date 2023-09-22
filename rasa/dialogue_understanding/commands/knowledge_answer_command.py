from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List
from rasa.dialogue_understanding.commands import FreeFormAnswerCommand
from rasa.dialogue_understanding.stack.dialogue_stack import DialogueStack
from rasa.dialogue_understanding.stack.frames.search_frame import SearchStackFrame
from rasa.shared.core.constants import DIALOGUE_STACK_SLOT
from rasa.shared.core.events import Event, SlotSet
from rasa.shared.core.flows.flow import FlowsList
from rasa.shared.core.trackers import DialogueStateTracker


@dataclass
class KnowledgeAnswerCommand(FreeFormAnswerCommand):
    """A command to indicate a knowledge-based free-form answer by the bot."""

    @classmethod
    def command(cls) -> str:
        """Returns the command type."""
        return "knowledge"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> KnowledgeAnswerCommand:
        """Converts the dictionary to a command.

        Returns:
            The converted dictionary.
        """
        return KnowledgeAnswerCommand()

    def run_command_on_tracker(
        self,
        tracker: DialogueStateTracker,
        all_flows: FlowsList,
        original_tracker: DialogueStateTracker,
    ) -> List[Event]:
        """Runs the command on the tracker.

        Args:
            tracker: The tracker to run the command on.
            all_flows: All flows in the assistant.
            original_tracker: The tracker before any command was executed.

        Returns:
            The events to apply to the tracker.
        """
        dialogue_stack = DialogueStack.from_tracker(tracker)
        dialogue_stack.push(SearchStackFrame())
        return [SlotSet(DIALOGUE_STACK_SLOT, dialogue_stack.as_dict())]