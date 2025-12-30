"""In-memory pub/sub message bus for agent coordination."""

from collections import defaultdict
from collections.abc import Callable
from typing import Any

from utils.logger import get_logger

Subscriber = Callable[[dict[str, Any]], None]


class MessageBus:
    """Simple publish/subscribe message bus."""

    def __init__(self) -> None:
        self.subscribers: defaultdict[str, list[Subscriber]] = defaultdict(list)
        self.messages: list[dict[str, Any]] = []
        self.logger = get_logger("message_bus")

    def subscribe(self, topic: str, handler: Subscriber) -> None:
        """Subscribe a handler to a topic."""
        self.subscribers[topic].append(handler)

    def publish(self, topic: str, payload: dict[str, Any]) -> None:
        """Publish a payload to all subscribers of a topic."""
        message = {"topic": topic, "payload": payload}
        self.messages.append(message)
        for handler in self.subscribers.get(topic, []):
            handler(payload)
        self.logger.info("Published message on topic: %s", topic)
