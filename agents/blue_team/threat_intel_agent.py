"""Threat intelligence simulation agent."""

from typing import Any

from agents.base_agent import BaseAgent
from mitre_integration.attack_mapping import map_actions_to_ttp
from utils.prompt_templates import THREAT_INTEL_PROMPT


class ThreatIntelAgent(BaseAgent):
    """Simulated threat intelligence agent for attribution and mapping."""

    def __init__(self) -> None:
        super().__init__(
            name="ThreatIntelAgent",
            role="Threat Intelligence",
            system_prompt=THREAT_INTEL_PROMPT,
            tools=["ttp_mapper", "attribution_simulator"],
        )

    def execute_task(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Execute a simulated threat intelligence task."""
        plan = self.plan_action(objective, context)
        ttp_matches = map_actions_to_ttp(plan["proposed_actions"] + ["intel"])
        output = self.generate_output(objective, ttp_matches)
        output["assessment"] = {
            "confidence": "medium",
            "notes": "Simulated attribution based on TTP overlap and sector targeting trends.",
        }
        self.logger.info("Threat intel output generated for objective: %s", objective)
        return output
