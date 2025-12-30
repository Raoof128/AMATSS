"""Report generation utilities."""

import json
from pathlib import Path
from typing import Any

from utils.logger import get_logger

LOGGER = get_logger("reporting")


def write_report(report_path: Path, report: dict[str, Any]) -> None:
    """Write a JSON report to disk."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with report_path.open("w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, ensure_ascii=True)
    except OSError as exc:
        LOGGER.error("Failed to write report: %s", exc)


def write_markdown_summary(report_path: Path, report: dict[str, Any]) -> None:
    """Write a Markdown summary from a report."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    md = [
        "# Simulation Summary",
        "",
        f"**Scenario:** {report['scenario']['name']}",
        f"**Sector:** {report['scenario']['sector']}",
        "",
        "## Key Findings",
    ]
    md.extend([f"- {item}" for item in report.get("key_findings", [])])
    md.append("")
    md.append("## MITRE ATT&CK Coverage")
    for ttp in report.get("ttp_summary", []):
        md.append(f"- {ttp['id']} {ttp['name']} ({ttp['tactic']})")
    md.append("")
    md.append("## Defensive Recommendations")
    md.extend([f"- {item}" for item in report.get("recommendations", [])])

    try:
        with report_path.open("w", encoding="utf-8") as handle:
            handle.write("\n".join(md) + "\n")
    except OSError as exc:
        LOGGER.error("Failed to write markdown summary: %s", exc)
