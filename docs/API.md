# API Documentation

This project exposes internal Python APIs used for simulation orchestration.

## Coordinator

```python
from orchestration.coordinator import Coordinator

coordinator = Coordinator(log_path="logs/simulation.log", session_db_path="logs/sessions.db")
result = coordinator.run("soci_energy_grid", rounds=3)
```

**run(scenario_id: str, rounds: int) -> SimulationResult**
- Runs the simulation for the specified scenario and number of rounds.
- Returns a `SimulationResult` with outputs and session_id.

## SessionStore

```python
from storage.session_store import SessionStore
store = SessionStore(Path("logs/sessions.db"))
```

**create_session(session_id, scenario_id, created_at)**
- Creates a new session record.

**append_event(session_id, actor, event_type, payload)**
- Persists a structured event.

**list_events(session_id) -> list**
- Returns all events for a session.

## VectorStore

```python
from storage.vector_store import VectorStore
store = VectorStore()
store.add_documents(["doc1"], ["example text"])
```

**add_documents(ids, texts)**
- Adds documents if Chroma is installed.

**query(query_text, top_k=3)**
- Returns matching documents or empty list if unavailable.
