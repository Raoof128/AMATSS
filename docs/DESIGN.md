# Design Notes

## Clean Architecture
- **Domain**: Agents, scenarios, MITRE mappings
- **Application**: Orchestration coordinator and state
- **Infrastructure**: SQLite session store, logging, Streamlit UI

## Key Design Decisions
- Simulation-only policy enforced at agent base class
- Structured logging with JSON lines
- Minimal external dependencies for portability

## Extensibility
- Add new scenarios in `scenarios/`
- Add tools or LLM integrations in agent subclasses
- Replace in-memory message bus with MCP server if needed
