# Contributing

Thanks for your interest in contributing.

## Development Setup
1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install dev dependencies: `pip install -r requirements-dev.txt`

## Running the Project
- `python main.py --scenario soci_energy_grid --rounds 3`
- `streamlit run dashboard/streamlit_ui.py`

## Code Standards
- Python 3.11+
- Type hints required
- Docstrings required for all public functions and classes
- Use `ruff` for linting and formatting (`ruff check .`, `ruff format .`)

## Tests
- `pytest`

## Pull Request Checklist
- [ ] Added/updated tests
- [ ] Updated documentation
- [ ] Confirmed simulation-only behavior
