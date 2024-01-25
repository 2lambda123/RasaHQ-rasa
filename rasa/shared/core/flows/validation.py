from __future__ import annotations

from collections import defaultdict
import re
from typing import Optional, Set, Text, List

from rasa.shared.core.flows.flow_step import (
    FlowStep,
)
from rasa.shared.core.flows.flow_step_links import (
    BranchingFlowStepLink,
    IfFlowStepLink,
    ElseFlowStepLink,
)
from rasa.shared.core.flows.flow_step_sequence import FlowStepSequence
from rasa.shared.core.flows.steps.constants import CONTINUE_STEP_PREFIX, DEFAULT_STEPS
from rasa.shared.core.flows.steps.link import LinkFlowStep
from rasa.shared.core.flows.steps.collect import CollectInformationFlowStep
from rasa.shared.core.flows.flow import Flow
from rasa.shared.exceptions import RasaException


class UnreachableFlowStepException(RasaException):
    """Raised when a flow step is unreachable."""

    def __init__(self, step_id: str, flow_id: str) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Step '{self.step_id}' in flow '{self.flow_id}' can not be reached "
            f"from the start step. Please make sure that all steps can be reached "
            f"from the start step, e.g. by "
            f"checking that another step points to this step."
        )


class MissingNextLinkException(RasaException):
    """Raised when a flow step is missing a next link."""

    def __init__(self, step_id: str, flow_id: str) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Step '{self.step_id}' in flow '{self.flow_id}' is missing a `next`. "
            f"As a last step of a branch, it is required to have one. "
        )


class ReservedFlowStepIdException(RasaException):
    """Raised when a flow step is using a reserved id."""

    def __init__(self, step_id: str, flow_id: str) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Step '{self.step_id}' in flow '{self.flow_id}' is using the reserved id "
            f"'{self.step_id}'. Please use a different id for your step."
        )


class MissingElseBranchException(RasaException):
    """Raised when a flow step is missing an else branch."""

    def __init__(self, step_id: str, flow_id: str) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Step '{self.step_id}' in flow '{self.flow_id}' is missing an `else` "
            f"branch. If a steps `next` statement contains an `if` it always "
            f"also needs an `else` branch. Please add the missing `else` branch."
        )


class NoNextAllowedForLinkException(RasaException):
    """Raised when a flow step has a next link but is not allowed to have one."""

    def __init__(self, step_id: str, flow_id: str) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Link step '{self.step_id}' in flow '{self.flow_id}' has a `next` but "
            f"as a link step is not allowed to have one."
        )


class UnresolvedFlowStepIdException(RasaException):
    """Raised when a flow step is referenced, but its id can not be resolved."""

    def __init__(
        self, step_id: str, flow_id: str, referenced_from_step_id: Optional[str]
    ) -> None:
        """Initializes the exception."""
        self.step_id = step_id
        self.flow_id = flow_id
        self.referenced_from_step_id = referenced_from_step_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        if self.referenced_from_step_id:
            exception_message = (
                f"Step with id '{self.step_id}' could not be resolved. "
                f"'Step '{self.referenced_from_step_id}' in flow '{self.flow_id}' "
                f"referenced this step but it does not exist. "
            )
        else:
            exception_message = (
                f"Step '{self.step_id}' in flow '{self.flow_id}' can not be resolved. "
            )

        return exception_message + (
            "Please make sure that the step is defined in the same flow."
        )


class EmptyStepSequenceException(RasaException):
    """Raised when an empty step sequence is encountered."""

    def __init__(self, flow_id: str, step_id: str) -> None:
        """Initializes the exception."""
        self.flow_id = flow_id
        self.step_id = step_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Encountered an empty step sequence in flow '{self.flow_id}' "
            f"and step '{self.step_id}'."
        )


class EmptyFlowException(RasaException):
    """Raised when a flow is completely empty."""

    def __init__(self, flow_id: str) -> None:
        """Initializes the exception."""
        self.flow_id = flow_id

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return f"Flow '{self.flow_id}' does not have any steps."


class DuplicateNLUTriggerException(RasaException):
    """Raised when multiple flows can be started by the same intent."""

    def __init__(self, intent: str, flow_names: List[str]) -> None:
        """Initializes the exception."""
        self.intent = intent
        self.flow_names = flow_names

    def __str__(self) -> Text:
        """Return a string representation of the exception."""
        return (
            f"The intent '{self.intent}' is used as 'nlu_trigger' "
            f"in multiple flows: {self.flow_names}."
            f"An intent should just trigger one flow, not multiple."
        )


class SlotNamingException(RasaException):
    """Raised when a slot name to be collected does not adhere to naming convention."""

    def __init__(self, flow_id: str, step_id: str, slot_name: str) -> None:
        """Initializes the exception."""
        self.flow_id = flow_id
        self.step_id = step_id
        self.slot_name = slot_name

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"For the flow '{self.flow_id}', collect step '{self.step_id}' "
            f"the slot name was set to : {self.slot_name}, while it has "
            f"to adhere to the following pattern: [a-zA-Z_][a-zA-Z0-9_-]*?."
        )


def validate_flow(flow: Flow) -> None:
    """Validates the flow configuration.

    This ensures that the flow semantically makes sense. E.g. it
    checks:
        - whether all next links point to existing steps
        - whether all steps can be reached from the start step
    """
    validate_flow_not_empty(flow)
    validate_no_empty_step_sequences(flow)
    validate_all_steps_next_property(flow)
    validate_all_next_ids_are_available_steps(flow)
    validate_all_steps_can_be_reached(flow)
    validate_all_branches_have_an_else(flow)
    validate_not_using_builtin_ids(flow)
    validate_slot_names_to_be_collected(flow)


def validate_flow_not_empty(flow: Flow) -> None:
    """Validate that the flow is not empty."""
    if len(flow.steps) == 0:
        raise EmptyFlowException(flow.id)


def validate_no_empty_step_sequences(flow: Flow) -> None:
    """Validate that the flow does not have any empty step sequences."""
    for step in flow.steps:
        for link in step.next.links:
            if (
                isinstance(link, BranchingFlowStepLink)
                and isinstance(link.target_reference, FlowStepSequence)
                and len(link.target_reference.child_steps) == 0
            ):
                raise EmptyStepSequenceException(flow.id, step.id)


def validate_not_using_builtin_ids(flow: Flow) -> None:
    """Validates that the flow does not use any of the build in ids."""
    for step in flow.steps:
        if step.id in DEFAULT_STEPS or step.id.startswith(CONTINUE_STEP_PREFIX):
            raise ReservedFlowStepIdException(step.id, flow.id)


def validate_all_branches_have_an_else(flow: Flow) -> None:
    """Validates that all branches have an else link."""
    for step in flow.steps:
        links = step.next.links

        has_an_if = any(isinstance(link, IfFlowStepLink) for link in links)
        has_an_else = any(isinstance(link, ElseFlowStepLink) for link in links)

        if has_an_if and not has_an_else:
            raise MissingElseBranchException(step.id, flow.id)


def validate_all_steps_next_property(flow: Flow) -> None:
    """Validates that every step that must have a `next` has one."""
    for step in flow.steps:
        if isinstance(step, LinkFlowStep):
            # link steps can't have a next link!
            if not step.next.no_link_available():
                raise NoNextAllowedForLinkException(step.id, flow.id)
        elif step.next.no_link_available():
            # all other steps should have a next link
            raise MissingNextLinkException(step.id, flow.id)


def validate_all_next_ids_are_available_steps(flow: Flow) -> None:
    """Validates that all next links point to existing steps."""
    available_steps = {step.id for step in flow.steps} | DEFAULT_STEPS
    for step in flow.steps:
        for link in step.next.links:
            if link.target not in available_steps:
                raise UnresolvedFlowStepIdException(link.target, flow.id, step.id)


def validate_all_steps_can_be_reached(flow: Flow) -> None:
    """Validates that all steps can be reached from the start step."""

    def _reachable_steps(
        step: Optional[FlowStep], reached_steps: Set[Text]
    ) -> Set[Text]:
        """Validates that the given step can be reached from the start step."""
        if step is None or step.id in reached_steps:
            return reached_steps

        reached_steps.add(step.id)
        for link in step.next.links:
            reached_steps = _reachable_steps(
                flow.step_by_id(link.target), reached_steps
            )
        return reached_steps

    reached_steps = _reachable_steps(flow.first_step_in_flow(), set())

    for step in flow.steps:
        if step.id not in reached_steps:
            raise UnreachableFlowStepException(step.id, flow.id)


def validate_nlu_trigger(flows: List[Flow]) -> None:
    """Validates that an intent can just trigger one flow."""
    nlu_trigger_to_flows = defaultdict(list)

    for flow in flows:
        intents = flow.get_trigger_intents()
        for intent in intents:
            nlu_trigger_to_flows[intent].append(flow.name)

    for intent, flow_names in nlu_trigger_to_flows.items():
        if len(flow_names) > 1:
            raise DuplicateNLUTriggerException(intent, flow_names)


def validate_slot_names_to_be_collected(flow: Flow) -> None:
    """Validates that slot names to be collected comply with a specified regex."""
    slot_re = re.compile(r"""^[a-zA-Z_][a-zA-Z0-9_-]*?$""")
    for step in flow.steps:
        if isinstance(step, CollectInformationFlowStep):
            slot_name = step.collect
            if not slot_re.search(slot_name):
                raise SlotNamingException(flow.id, step.id, slot_name)