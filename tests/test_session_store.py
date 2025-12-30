from pathlib import Path

from storage.session_store import SessionStore


def test_session_store_persists_events(tmp_path: Path) -> None:
    db_path = tmp_path / "sessions.db"
    store = SessionStore(db_path)
    store.create_session("session-1", "soci_energy_grid", "2025-01-01T00:00:00Z")
    store.append_event("session-1", "Agent", "test_event", {"foo": "bar"})
    events = store.list_events("session-1")
    assert events[0]["actor"] == "Agent"
