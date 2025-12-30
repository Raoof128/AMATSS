"""Base agent implementation shared by red and blue team agents."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from utils.logger import get_logger


@dataclass
class AgentMemory:
    """In-memory conversation and episodic memory."""

    conversation: list[dict[str, Any]] = field(default_factory=list)
    episodic: list[dict[str, Any]] = field(default_factory=list)


class BaseAgent(ABC):
    """Base agent with memory and simulation-only planning."""

    def __init__(self, name: str, role: str, system_prompt: str, tools: list[str]) -> None:
        if not name or not role:
            raise ValueError("Agent name and role must be provided.")
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.tools = tools
        self.memory = AgentMemory()
        self.logger = get_logger(f"agent.{name}")

    def record_event(self, event: dict[str, Any]) -> None:
        """Record an event in conversation memory."""
        self.memory.conversation.append(event)

    def record_episode(self, summary: dict[str, Any]) -> None:
        """Record a summary in episodic memory."""
        self.memory.episodic.append(summary)

    def plan_action(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Produce a simulation-only plan for the given objective."""
        if not objective:
            raise ValueError("Objective must be a non-empty string.")
        plan = {
            "agent": self.name,
            "role": self.role,
            "objective": objective,
            "constraints": "simulation-only, no real exploitation",
            "context": context,
            "proposed_actions": [
                "Analyze scenario context",
                "Reference relevant MITRE ATT&CK techniques",
                "Produce simulated findings and recommendations",
            ],
        }
        self.record_event({"type": "plan", "content": plan})
        return plan

    def generate_output(self, objective: str, ttp_matches: list[dict[str, str]]) -> dict[str, Any]:
        """Generate a structured, simulation-only output payload."""
        output = {
            "agent": self.name,
            "summary": f"Simulated output for objective: {objective}",
            "ttp_matches": ttp_matches,
            "safety": "No real actions taken; documentation-only simulation.",
        }
        self.record_event({"type": "output", "content": output})
        return output

    @abstractmethod
    def execute_task(self, objective: str, context: dict[str, Any]) -> dict[str, Any]:
        """Execute the agent's simulation task."""
        raise NotImplementedError
