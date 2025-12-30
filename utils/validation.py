"""Input validation helpers for CLI and orchestration."""

from collections.abc import Iterable


def validate_rounds(rounds: int) -> int:
    """Validate rounds count.

    Args:
        rounds: Requested number of rounds.

    Returns:
        Validated rounds.

    Raises:
        ValueError: If rounds is not within valid bounds.
    """
    if rounds < 1:
        raise ValueError("Rounds must be >= 1.")
    if rounds > 50:
        raise ValueError("Rounds must be <= 50 for safety limits.")
    return rounds


def validate_scenario_id(scenario_id: str, available: Iterable[str]) -> str:
    """Validate scenario id against available ids.

    Args:
        scenario_id: Scenario identifier provided by the user.
        available: Iterable of available scenario ids.

    Returns:
        Validated scenario id.

    Raises:
        ValueError: If scenario id is not available.
    """
    options = list(available)
    if scenario_id not in options:
        raise ValueError(f"Unknown scenario '{scenario_id}'. Available: {', '.join(options)}")
    return scenario_id
