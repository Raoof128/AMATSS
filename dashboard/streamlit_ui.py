"""Streamlit dashboard for simulation visibility."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.logger import get_logger  # noqa: E402

LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "simulation.log"
LOGGER = get_logger("dashboard")


def load_events() -> list[dict]:
    """Load JSONL events from the log file."""
    if not LOG_PATH.exists():
        return []
    try:
        with LOG_PATH.open("r", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]
    except OSError as exc:
        LOGGER.error("Failed to read log file: %s", exc)
        return []


st.set_page_config(page_title="SOCI Agentic Simulation", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap');
    :root {
        --ink: #0f172a;
        --muted: #516072;
        --cream: #f8f1e8;
        --mist: #e6eef6;
        --accent: #ff6b4a;
        --accent-2: #21b3a8;
        --card: #ffffff;
    }
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, var(--cream), transparent 45%),
            radial-gradient(circle at 90% 0%, #ffe0d7, transparent 50%),
            linear-gradient(180deg, var(--mist), #f7f8fb 65%);
        color: var(--ink);
    }
    .app-shell {
        padding: 1.5rem 1.5rem 0;
    }
    .headline {
        font-family: "DM Serif Display", serif;
        font-size: clamp(2rem, 2.8vw, 3rem);
        line-height: 1.05;
        margin-bottom: 0.35rem;
    }
    .tagline {
        color: var(--muted);
        font-family: "Space Grotesk", sans-serif;
        font-size: 1rem;
        letter-spacing: 0.04em;
    }
    .subhead {
        font-family: "Space Grotesk", sans-serif;
        font-weight: 600;
        margin: 1.5rem 0 0.5rem;
    }
    .card {
        background: var(--card);
        border-radius: 16px;
        padding: 1.1rem;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
        border: 1px solid rgba(15, 23, 42, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 22px 55px rgba(15, 23, 42, 0.12);
    }
    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.3rem 0.7rem;
        border-radius: 999px;
        font-size: 0.75rem;
        background: rgba(33, 179, 168, 0.12);
        color: #0f766e;
        font-family: "Space Grotesk", sans-serif;
        font-weight: 600;
    }
    .metric {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }
    .muted {
        color: var(--muted);
        font-size: 0.9rem;
    }
    .divider {
        height: 1px;
        background: rgba(15, 23, 42, 0.08);
        margin: 1.5rem 0 1rem;
    }
    .legend {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 0.75rem;
    }
    .legend-item {
        padding: 0.7rem 0.8rem;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(15, 23, 42, 0.06);
        font-family: "Space Grotesk", sans-serif;
    }
    .legend-item strong {
        display: block;
        margin-bottom: 0.25rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='app-shell'>", unsafe_allow_html=True)
st.markdown("<div class='pill'>Simulation-only</div>", unsafe_allow_html=True)
st.markdown("<div class='headline'>Autonomous Red/Blue Team Simulation</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='tagline'>SOCI Act critical infrastructure | research-grade safety harness</div>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        "<div class='card'><strong>Active Agents</strong>"
        "<div class='metric'>7</div>"
        "<div class='muted'>4 red + 3 blue</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        "<div class='card'><strong>Kill Chain Progress</strong>"
        "<div class='metric'>3/5</div>"
        "<div class='muted'>Recon → Access → Movement</div></div>",
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        "<div class='card'><strong>Compliance Focus</strong>"
        "<div class='metric'>A+</div>"
        "<div class='muted'>SOCI Act + ASD Essential Eight</div></div>",
        unsafe_allow_html=True,
    )

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='subhead'>Live Event Stream</div>", unsafe_allow_html=True)

events = load_events()
if not events:
    st.info("No events yet. Run `python main.py` to generate simulation logs.")
else:
    df = pd.DataFrame(events)
    st.dataframe(df, use_container_width=True, height=340)

st.markdown("<div class='subhead'>MITRE ATT&CK Heatmap (Simulated)</div>", unsafe_allow_html=True)
heatmap_data = pd.DataFrame(
    {
        "Tactic": ["Reconnaissance", "Initial Access", "Lateral Movement", "Defense Evasion"],
        "Signal": [4, 3, 2, 1],
    }
)
st.bar_chart(heatmap_data.set_index("Tactic"))

st.markdown("<div class='subhead'>Operational Highlights</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='legend'>
        <div class='legend-item'>
            <strong>Primary Objective</strong>
            Simulate attack paths across SOCI scenarios without operational risk.
        </div>
        <div class='legend-item'>
            <strong>Blue Team Lens</strong>
            Prioritize ASD Essential Eight mitigations and SOCI reporting windows.
        </div>
        <div class='legend-item'>
            <strong>Report Output</strong>
            JSON + Markdown executive summary for compliance briefings.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
