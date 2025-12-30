"""Response simulation agent."""

from typing import Any

from agents.base_agent import BaseAgent
from mitre_integration.attack_mapping import map_actions_to_ttp
from utils.prompt_templates import RESPONSE_PROMPT


class ResponseAgent(BaseAgent):
    """Simulated response agent for containment and remediation."""

    def __init__(self) -> None:
        super().__init__(
            name="ResponseAgent",
            role="Response",
            system_prompt=RESPONSE_PROMPT,
            tools=["containment_planner", "remediation_builder"],
        )

    def execute_task(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Execute a simulated response task."""
        plan = self.plan_action(objective, context)
        ttp_matches = map_actions_to_ttp(plan["proposed_actions"] + ["respond"])
        output = self.generate_output(objective, ttp_matches)
        output["playbook"] = [
            "Isolate affected segments per SOCI escalation",
            "Enforce MFA resets and credential hygiene",
            "OT safety checks before restoration",
        ]
        output["asd_essential_eight"] = [
            "Application control",
            "Patch applications",
            "Restrict administrative privileges",
        ]
        self.logger.info("Response output generated for objective: %s", objective)
        return output
