"""Social engineering simulation agent."""

from typing import Any

from agents.base_agent import BaseAgent
from mitre_integration.attack_mapping import map_actions_to_ttp
from utils.prompt_templates import SOCIAL_ENGINEERING_PROMPT


class SocialEngineeringAgent(BaseAgent):
    """Simulated social engineering agent."""

    def __init__(self) -> None:
        super().__init__(
            name="SocialEngineeringAgent",
            role="Social Engineering",
            system_prompt=SOCIAL_ENGINEERING_PROMPT,
            tools=["phishing_simulator", "pretext_builder"],
        )

    def execute_task(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Execute a simulated social engineering task."""
        plan = self.plan_action(objective, context)
        ttp_matches = map_actions_to_ttp(plan["proposed_actions"] + ["phishing"])
        output = self.generate_output(objective, ttp_matches)
        output["campaign_concepts"] = [
            "Supplier invoice change pretext (training-only)",
            "Credential hygiene awareness scenario",
            "Executive access confirmation simulation",
        ]
        self.logger.info("Social engineering output generated for objective: %s", objective)
        return output
