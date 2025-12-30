"""Water system SOCI scenario definition."""

from scenarios.types import Scenario

SCENARIO: Scenario = {
    "id": "soci_water_system",
    "name": "Water Treatment Facility Intrusion",
    "sector": "Water",
    "description": "ICS-focused intrusion simulation targeting treatment operations.",
    "objectives": [
        "Document potential access paths to ICS management",
        "Simulate operator credential misuse scenario",
        "Assess impact to safety and water quality monitoring",
    ],
    "constraints": [
        "Simulation-only",
        "No operational ICS commands",
        "Safety and regulatory compliance emphasis",
    ],
}
