"""State manager for simulation sessions."""

from typing import Any

from utils.logger import get_logger


class StateManager:
    """Manage mutable simulation state with event tracking."""

    def __init__(self) -> None:
        self.state: dict[str, Any] = {
            "round": 0,
            "scenario": None,
            "red_team": {},
            "blue_team": {},
            "events": [],
        }
        self.logger = get_logger("state_manager")

    def update(self, key: str, value: Any) -> None:
        """Update a state key."""
        self.state[key] = value
        self.logger.debug("State updated: %s", key)

    def append_event(self, event: dict[str, Any]) -> None:
        """Append an event to the event list."""
        self.state["events"].append(event)
        self.logger.debug("Event appended")

    def snapshot(self) -> dict[str, Any]:
        """Return a shallow copy of current state."""
        return dict(self.state)
