import pytest

from utils.validation import validate_rounds, validate_scenario_id


def test_validate_rounds_bounds() -> None:
    assert validate_rounds(1) == 1
    assert validate_rounds(50) == 50
    with pytest.raises(ValueError):
        validate_rounds(0)
    with pytest.raises(ValueError):
        validate_rounds(51)


def test_validate_scenario_id() -> None:
    assert validate_scenario_id("a", ["a", "b"]) == "a"
    with pytest.raises(ValueError):
        validate_scenario_id("c", ["a", "b"])
