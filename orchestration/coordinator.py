"""Coordinator for orchestrating red/blue team simulation rounds."""

from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from agents.blue_team.detection_agent import DetectionAgent
from agents.blue_team.response_agent import ResponseAgent
from agents.blue_team.threat_intel_agent import ThreatIntelAgent
from agents.red_team.exploitation_agent import ExploitationAgent
from agents.red_team.lateral_movement_agent import LateralMovementAgent
from agents.red_team.recon_agent import ReconAgent
from agents.red_team.social_engineering_agent import SocialEngineeringAgent
from orchestration.message_bus import MessageBus
from orchestration.state_manager import StateManager
from orchestration.types import SimulationResult
from scenarios import SCENARIOS, get_scenario
from storage.session_store import SessionStore
from utils.logger import get_logger
from utils.logging_handler import JsonLogger


class Coordinator:
    """Primary simulation coordinator."""

    def __init__(self, log_path: str, session_db_path: str) -> None:
        self.message_bus = MessageBus()
        self.state = StateManager()
        self.logger = JsonLogger(log_path=log_path)
        self.app_logger = get_logger("coordinator")
        self.session_store = SessionStore(db_path=session_db_path)
        self.red_agents = [
            ReconAgent(),
            SocialEngineeringAgent(),
            ExploitationAgent(),
            LateralMovementAgent(),
        ]
        self.blue_agents = [
            DetectionAgent(),
            ResponseAgent(),
            ThreatIntelAgent(),
        ]

    def run(self, scenario_id: str, rounds: int) -> SimulationResult:
        """Run the simulation for a scenario over N rounds."""
        if rounds < 1:
            raise ValueError("Rounds must be >= 1.")
        if scenario_id not in SCENARIOS:
            self.app_logger.warning(
                "Unknown scenario '%s', defaulting to energy grid.", scenario_id
            )
        scenario = get_scenario(scenario_id)
        self.state.update("scenario", scenario)
        self.logger.emit("Coordinator", "scenario_init", "Scenario initialized", scenario)
        session_id = str(uuid4())
        created_at = datetime.now(UTC).isoformat()
        self.session_store.create_session(session_id, scenario["id"], created_at)

        red_outputs: list[dict[str, Any]] = []
        blue_outputs: list[dict[str, Any]] = []
        events: list[dict[str, Any]] = []

        for round_index in range(1, rounds + 1):
            self.state.update("round", round_index)
            self.logger.emit("Coordinator", "round_start", f"Round {round_index} start")

            for agent in self.red_agents:
                objective = scenario["objectives"][
                    min(round_index - 1, len(scenario["objectives"]) - 1)
                ]
                output = agent.execute_task(objective, {"scenario": scenario})
                red_outputs.append(output)
                event = {"team": "red", "agent": agent.name, "output": output}
                events.append(event)
                self.state.append_event(event)
                self.logger.emit(agent.name, "red_action", output["summary"], output)
                self.session_store.append_event(session_id, agent.name, "red_action", output)

            for agent in self.blue_agents:
                objective = "Detect and respond to simulated red team activity"
                output = agent.execute_task(
                    objective, {"scenario": scenario, "red_team": red_outputs[-4:]}
                )
                blue_outputs.append(output)
                event = {"team": "blue", "agent": agent.name, "output": output}
                events.append(event)
                self.state.append_event(event)
                self.logger.emit(agent.name, "blue_action", output["summary"], output)
                self.session_store.append_event(session_id, agent.name, "blue_action", output)

            self.logger.emit("Coordinator", "round_end", f"Round {round_index} end")
        self.app_logger.info("Simulation complete for session %s", session_id)

        return SimulationResult(
            scenario=scenario,
            red_team=red_outputs,
            blue_team=blue_outputs,
            events=events,
            session_id=session_id,
        )
