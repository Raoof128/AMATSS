"""Telecommunications SOCI scenario definition."""

from scenarios.types import Scenario

SCENARIO: Scenario = {
    "id": "soci_telco_network",
    "name": "Telecommunications Network Compromise",
    "sector": "Telecommunications",
    "description": "Supply chain angle targeting carrier infrastructure and core services.",
    "objectives": [
        "Identify exposure in supplier-managed systems",
        "Simulate credential harvesting via partner portal",
        "Assess risks to customer metadata and routing control",
    ],
    "constraints": [
        "Simulation-only",
        "No real phishing or credential testing",
        "Privacy Act 1988 considerations",
    ],
}
