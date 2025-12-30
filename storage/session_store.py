"""SQLite-backed session persistence for simulations."""

import json
import sqlite3
from pathlib import Path
from typing import Any

from utils.logger import get_logger


class SessionStore:
    """Persist simulation sessions and events to SQLite."""

    def __init__(self, db_path: Path | str) -> None:
        self.db_path = Path(db_path)
        self.logger = get_logger("session_store")
        self._init_db()

    def _init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS sessions (
                    id TEXT PRIMARY KEY,
                    scenario_id TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    actor TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    FOREIGN KEY(session_id) REFERENCES sessions(id)
                )
                """
            )

    def create_session(self, session_id: str, scenario_id: str, created_at: str) -> None:
        """Create a new session record."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO sessions (id, scenario_id, created_at) VALUES (?, ?, ?)",
                (session_id, scenario_id, created_at),
            )
        self.logger.info("Created session %s", session_id)

    def append_event(
        self, session_id: str, actor: str, event_type: str, payload: dict[str, Any]
    ) -> None:
        """Append a structured event for a session."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO events (session_id, actor, event_type, payload) VALUES (?, ?, ?, ?)",
                (session_id, actor, event_type, json.dumps(payload, ensure_ascii=True)),
            )
        self.logger.debug("Event persisted for session %s", session_id)

    def list_events(self, session_id: str) -> list[dict[str, Any]]:
        """Return all events for a session."""
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT actor, event_type, payload FROM events WHERE session_id = ? ORDER BY id",
                (session_id,),
            ).fetchall()
        return [
            {"actor": actor, "event_type": event_type, "payload": json.loads(payload)}
            for actor, event_type, payload in rows
        ]
