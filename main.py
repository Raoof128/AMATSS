"""CLI entrypoint for running the simulation."""

import argparse

from config import APP_CONFIG, LOG_DIR, REPORT_DIR, SESSION_DB_PATH
from orchestration.coordinator import Coordinator
from orchestration.types import SimulationResult
from scenarios import SCENARIOS
from utils.logger import get_logger, set_root_log_level
from utils.reporting import write_markdown_summary, write_report
from utils.validation import validate_rounds, validate_scenario_id


def build_report(simulation: SimulationResult) -> dict:
    """Build a summary report from simulation outputs."""
    ttp_summary: list[dict[str, str]] = []
    for output in simulation.red_team + simulation.blue_team:
        ttp_summary.extend(output.get("ttp_matches", []))

    unique_ttp = {f"{ttp['id']}-{ttp['name']}": ttp for ttp in ttp_summary}

    return {
        "scenario": simulation.scenario,
        "key_findings": [
            "Simulated attack paths demonstrate OT/IT convergence risk",
            "Social engineering remains high leverage against suppliers",
            "Detection telemetry gaps appear in cross-domain visibility",
        ],
        "ttp_summary": list(unique_ttp.values()),
        "recommendations": [
            "Align incident response workflows to SOCI Act reporting",
            "Implement ASD Essential Eight controls across suppliers",
            "Segment OT environments with strict access governance",
        ],
        "safety": "Simulation-only. No real exploitation, scanning, or payload execution.",
    }


def main() -> None:
    """Parse CLI args and run the simulation."""
    parser = argparse.ArgumentParser(description="Autonomous Red/Blue Team Simulation")
    parser.add_argument("--scenario", default=APP_CONFIG.scenario_default)
    parser.add_argument("--rounds", type=int, default=APP_CONFIG.max_rounds)
    parser.add_argument(
        "--list-scenarios", action="store_true", help="List available scenarios and exit."
    )
    args = parser.parse_args()

    set_root_log_level(APP_CONFIG.log_level)
    logger = get_logger("main", APP_CONFIG.log_level)
    if args.list_scenarios:
        for scenario_id, scenario in SCENARIOS.items():
            print(f"{scenario_id}: {scenario['name']}")
        return
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / "simulation.log"
    session_db_path = SESSION_DB_PATH

    coordinator = Coordinator(log_path=str(log_path), session_db_path=str(session_db_path))
    try:
        scenario_id = validate_scenario_id(args.scenario, SCENARIOS.keys())
        rounds = validate_rounds(args.rounds)
        simulation = coordinator.run(scenario_id, rounds)
    except ValueError as exc:
        logger.error("Simulation failed: %s", exc)
        raise SystemExit(1) from exc

    report = build_report(simulation)
    write_report(REPORT_DIR / "report.json", report)
    write_markdown_summary(REPORT_DIR / "summary.md", report)

    print("Simulation complete.")
    print(f"Log: {log_path}")
    print(f"Report: {REPORT_DIR / 'report.json'}")


if __name__ == "__main__":
    main()
