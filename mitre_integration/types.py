"""Typed structures for MITRE ATT&CK mapping."""

from typing import TypedDict


class TTP(TypedDict):
    """MITRE ATT&CK technique representation."""

    id: str
    name: str
    tactic: str
