from pathlib import Path

from orchestration.coordinator import Coordinator


def test_coordinator_runs(tmp_path: Path) -> None:
    log_path = tmp_path / "simulation.log"
    db_path = tmp_path / "sessions.db"
    coordinator = Coordinator(log_path=str(log_path), session_db_path=str(db_path))
    result = coordinator.run("soci_energy_grid", rounds=1)
    assert result.session_id
    assert result.scenario["id"] == "soci_energy_grid"
    assert len(result.red_team) == 4
    assert len(result.blue_team) == 3
