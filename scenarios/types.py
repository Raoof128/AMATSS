"""Scenario type definitions."""

from typing import TypedDict


class Scenario(TypedDict):
    """Scenario definition structure."""

    id: str
    name: str
    sector: str
    description: str
    objectives: list[str]
    constraints: list[str]
