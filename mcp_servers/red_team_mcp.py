"""Red team MCP server stub for inter-agent messaging."""

from typing import Any

from orchestration.message_bus import MessageBus


class RedTeamMCPServer:
    """Publish red team messages to the message bus."""

    def __init__(self, message_bus: MessageBus) -> None:
        self.message_bus = message_bus

    def send(self, payload: dict[str, Any]) -> None:
        """Send a payload to the red team topic."""
        self.message_bus.publish("red_team", payload)
