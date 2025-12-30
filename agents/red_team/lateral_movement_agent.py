"""Lateral movement simulation agent."""

from typing import Any

from agents.base_agent import BaseAgent
from mitre_integration.attack_mapping import map_actions_to_ttp
from utils.prompt_templates import LATERAL_MOVEMENT_PROMPT


class LateralMovementAgent(BaseAgent):
    """Simulated lateral movement agent."""

    def __init__(self) -> None:
        super().__init__(
            name="LateralMovementAgent",
            role="Lateral Movement",
            system_prompt=LATERAL_MOVEMENT_PROMPT,
            tools=["network_traversal_simulator", "persistence_planner"],
        )

    def execute_task(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Execute a simulated lateral movement task."""
        plan = self.plan_action(objective, context)
        ttp_matches = map_actions_to_ttp(plan["proposed_actions"] + ["lateral"])
        output = self.generate_output(objective, ttp_matches)
        output["movement_strategy"] = [
            "Simulated jump host traversal",
            "Privilege boundary mapping",
            "Persistence documentation with defensive counterpoints",
        ]
        self.logger.info("Lateral movement output generated for objective: %s", objective)
        return output
