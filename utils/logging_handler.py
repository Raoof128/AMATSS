"""Structured logging utilities."""

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from utils.logger import get_logger


@dataclass
class LogEvent:
    """Structured log event payload."""

    timestamp: str
    actor: str
    event_type: str
    summary: str
    details: dict[str, Any]


class JsonLogger:
    """Logger that writes JSON lines to a file and stdout."""

    def __init__(self, log_path: Path | str, level: str = "INFO") -> None:
        self.log_path = Path(log_path)
        self.logger = get_logger("simulation", level=level)

    def emit(
        self, actor: str, event_type: str, summary: str, details: dict[str, Any] | None = None
    ) -> None:
        """Emit a structured log line and persist to file.

        Args:
            actor: Actor emitting the event.
            event_type: Event type label.
            summary: Short summary of the event.
            details: Optional structured details.
        """
        details = details or {}
        event = LogEvent(
            timestamp=datetime.now(UTC).isoformat(),
            actor=actor,
            event_type=event_type,
            summary=summary,
            details=details,
        )
        payload = json.dumps(event.__dict__, ensure_ascii=True)
        self.logger.info(payload)
        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            with self.log_path.open("a", encoding="utf-8") as handle:
                handle.write(payload + "\n")
        except OSError as exc:
            self.logger.error("Failed to write log file: %s", exc)
