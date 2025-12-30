"""Application configuration and paths."""

from dataclasses import dataclass
from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent
DATA_DIR: Final[Path] = PROJECT_ROOT / "data"
LOG_DIR: Final[Path] = PROJECT_ROOT / "logs"
REPORT_DIR: Final[Path] = PROJECT_ROOT / "reports"
SESSION_DB_PATH: Final[Path] = LOG_DIR / "sessions.db"


@dataclass(frozen=True)
class LLMConfig:
    """LLM provider configuration."""

    provider: str = "anthropic"
    model: str = "claude-3-5-sonnet"
    temperature: float = 0.2


@dataclass(frozen=True)
class AppConfig:
    """Top-level app configuration."""

    environment: str = "dev"
    scenario_default: str = "soci_energy_grid"
    max_rounds: int = 6
    log_level: str = "INFO"
    llm: LLMConfig = LLMConfig()


APP_CONFIG: Final[AppConfig] = AppConfig()
