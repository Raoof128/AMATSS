# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

- Raouf: 2025-12-31 (Australia/Sydney) | scope: repo | summary: add AGENT.md to gitignore | files: .gitignore | verification: not run | follow-ups: remove AGENT.md from git tracking if desired
- Raouf: 2025-12-31 (Australia/Sydney) | scope: lint | summary: wrap dashboard headline markdown to satisfy ruff line length | files: dashboard/streamlit_ui.py | verification: not run | follow-ups: rerun ruff check .
- Raouf: 2025-12-31 (Australia/Sydney) | scope: ui | summary: polish Streamlit dashboard layout, typography, and visual hierarchy for desktop | files: dashboard/streamlit_ui.py | verification: not run | follow-ups: review in Streamlit on desktop
- Raouf: 2025-12-31 (Australia/Sydney) | scope: lint | summary: suppress ruff E402 for streamlit import ordering after sys.path injection | files: dashboard/streamlit_ui.py | verification: ruff check ., pytest | follow-ups: none
- Raouf: 2025-12-31 (Australia/Sydney) | scope: fix | summary: ensure dashboard can import project modules when run via streamlit | files: dashboard/streamlit_ui.py | verification: not run | follow-ups: rerun streamlit dashboard
- Raouf: 2025-12-31 (Australia/Sydney) | scope: audit | summary: add CI/dependabot, dev tooling, usage guide, and ruff-driven typing/formatting cleanup | files: .github/*, .editorconfig, requirements*.txt, pyproject.toml, README.md, CONTRIBUTING.md, docs/USAGE.md, agents/*, utils/*, dashboard/*, scenarios/__init__.py | verification: ruff check ., ruff format ., pytest | follow-ups: none
- Raouf: 2025-02-14 (Australia/Sydney) | scope: init | summary: initialize changelog and agent instructions | files: AGENT.md, CHANGELOG.md | verification: not run | follow-ups: implement baseline project structure
- Raouf: 2025-12-31 (Australia/Sydney) | scope: scaffold | summary: build initial agentic simulation framework and project layout | files: config.py, main.py, requirements.txt, README.md, agents/*, orchestration/*, mcp_servers/*, mitre_integration/*, scenarios/*, utils/*, dashboard/* | verification: not run | follow-ups: run main.py and streamlit dashboard
- Raouf: 2025-12-31 (Australia/Sydney) | scope: audit | summary: complete production-ready audit with docs, tests, storage, and refactors | files: config.py, main.py, README.md, requirements.txt, pyproject.toml, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, .gitignore, .env.example, docs/*, scripts/*, tests/*, storage/*, orchestration/*, utils/*, agents/*, scenarios/*, mitre_integration/*, dashboard/* | verification: not run | follow-ups: run pytest and demo scripts
- Raouf: 2025-12-31 (Australia/Sydney) | scope: validation | summary: add CLI validation, scenario listing, and tests | files: main.py, utils/validation.py, tests/test_validation.py, README.md | verification: not run | follow-ups: run pytest
- Raouf: 2025-12-31 (Australia/Sydney) | scope: tests | summary: add pytest path configuration for imports | files: tests/conftest.py | verification: not run | follow-ups: rerun pytest
- Raouf: 2025-12-31 (Australia/Sydney) | scope: bugfix | summary: handle string db paths in SessionStore | files: storage/session_store.py | verification: not run | follow-ups: rerun pytest
