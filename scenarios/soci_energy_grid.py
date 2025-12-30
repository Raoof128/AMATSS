"""Energy grid SOCI scenario definition."""

from scenarios.types import Scenario

SCENARIO: Scenario = {
    "id": "soci_energy_grid",
    "name": "Energy Grid Disruption",
    "sector": "Energy",
    "description": "OT/IT convergence attack simulation targeting grid control systems.",
    "objectives": [
        "Map external exposure of grid operator infrastructure",
        "Simulate supply chain foothold via vendor access",
        "Assess potential impact to SCADA oversight",
    ],
    "constraints": [
        "Simulation-only",
        "No real scanning or exploitation",
        "Respect SOCI Act reporting expectations",
    ],
}
