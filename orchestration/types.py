"""Types for orchestration layer."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SimulationResult:
    """Result payload for a simulation run."""

    scenario: dict[str, Any]
    red_team: list[dict[str, Any]]
    blue_team: list[dict[str, Any]]
    events: list[dict[str, Any]]
    session_id: str
