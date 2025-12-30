"""Scenario registry and access helpers."""

from scenarios.soci_energy_grid import SCENARIO as ENERGY_GRID
from scenarios.soci_telco_network import SCENARIO as TELCO
from scenarios.soci_water_system import SCENARIO as WATER
from scenarios.types import Scenario

SCENARIOS: dict[str, Scenario] = {
    ENERGY_GRID["id"]: ENERGY_GRID,
    TELCO["id"]: TELCO,
    WATER["id"]: WATER,
}


def get_scenario(scenario_id: str) -> Scenario:
    """Return a scenario by id or fall back to energy grid."""
    return SCENARIOS.get(scenario_id, ENERGY_GRID)
