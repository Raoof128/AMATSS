"""Helpers for mapping simulated actions to MITRE ATT&CK TTPs."""

from mitre_integration.ttp_database import DEFAULT_TTPS
from mitre_integration.types import TTP


def lookup_ttp(category: str) -> list[TTP]:
    """Return TTPs by category."""
    return DEFAULT_TTPS.get(category, [])


def map_actions_to_ttp(actions: list[str]) -> list[TTP]:
    """Infer TTPs from free-text actions."""
    keywords = " ".join(actions).lower()
    if "recon" in keywords or "osint" in keywords:
        return lookup_ttp("recon")
    if "phish" in keywords or "pretext" in keywords:
        return lookup_ttp("social")
    if "exploit" in keywords or "vulnerability" in keywords:
        return lookup_ttp("exploit")
    if "lateral" in keywords or "privilege" in keywords:
        return lookup_ttp("lateral")
    if "detect" in keywords or "alert" in keywords:
        return lookup_ttp("detection")
    if "respond" in keywords or "contain" in keywords:
        return lookup_ttp("response")
    if "intel" in keywords or "attribution" in keywords:
        return lookup_ttp("intel")
    return []
