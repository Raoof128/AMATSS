# Usage Guide

## CLI

List scenarios:

```bash
python main.py --list-scenarios
```

Run a simulation:

```bash
python main.py --scenario soci_energy_grid --rounds 3
```

## Outputs

After a run, the following artifacts are generated:
- `logs/simulation.log`: JSON line events for every agent action.
- `logs/sessions.db`: SQLite database with session metadata and events.
- `reports/report.json`: Structured final report.
- `reports/summary.md`: Markdown summary for portfolio use.

## Programmatic

```python
from orchestration.coordinator import Coordinator

coordinator = Coordinator(log_path="logs/simulation.log", session_db_path="logs/sessions.db")
result = coordinator.run("soci_water_system", rounds=2)
print(result.session_id)
```

## Dashboard

```bash
streamlit run dashboard/streamlit_ui.py
```
