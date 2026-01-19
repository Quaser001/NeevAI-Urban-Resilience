🌊 Neev AI – Urban Flood Intelligence System

Neev AI is an urban flood-risk decision intelligence platform designed for flood-prone Indian cities, with a pilot focus on Guwahati, Assam.

Unlike traditional flood maps that rely on static zones, Neev AI combines physics, historical flood memory, climate recurrence, and AI-assisted interpretation to answer a simple but critical question:

“Has this exact place flooded before, why did it flood, and what is likely to happen in the future?”

🚨 Problem Statement

Urban flooding in Indian cities is:

Highly localized (street-level, not district-level)

Poorly documented in official maps

Underestimated by buyers, renters, and even engineers

Increasingly severe due to climate change and urbanization

Existing solutions fail because they:

Depend on static flood zones

Ignore historical news-verified flooding

Provide no explanation or context

Are unusable for non-experts

💡 Neev AI – Core Idea

Neev AI treats flooding as a decidable phenomenon, not a binary label.

Every location is evaluated using:

Physical terrain constraints

Multi-year rainfall stress

Verified flood memory

Proximity-based impact propagation

Human-readable AI explanations

This allows risk assessment even if the exact coordinate was never officially mapped.

👥 Target Users
🏠 Buyers / Renters

“Did this exact street flood in the past?”

“Will my parking or ground floor get affected?”

“Is this risk occasional or chronic?”

👷 Engineers / Builders

“Is this site a drainage bowl?”

“Should basements be avoided?”

“What mitigation strategies are required?”

🧠 System Architecture (Agentic Design)

Neev AI is built as a multi-agent decision system.

Agent A – Physics (Deterministic)

Uses satellite-derived DEM (Digital Elevation Model)

Identifies low-lying terrain and drainage constraints

No AI hallucination — hard numbers only

Agent B – Climate Recurrence (Deterministic)

Scans 2020–2024 monsoon data

Counts extreme rainfall events (>50mm/day)

Captures stress recurrence, not single-year anomalies

Agent B2 – Flood Memory (Knowledge-Grounded)

Structured database built from:

News reports

Municipal disclosures

Resident-reported flooding

Stores:

Affected ward

Flood years

Severity

Impact radius

Enables statements like:

“This exact street flooded in 2022.”

Agent C – AI Consultant (Gemini)

Does not compute scores

Converts structured risk signals into:

Damage narratives

Resident impact explanations

2035 climate outlook

Fully grounded on Agent A/B/B2 outputs

🗺️ Mapping & Visualization

Neev AI provides multi-layer GIS intelligence:

Street Map – Navigation & locality context

Satellite Map – Built-up area & drainage patterns

Elevation (Topo) Map – Terrain & slope awareness

Flood Memory Overlays – Radius-based historical impact zones

Flood areas are intentionally modeled as zones, not points, because real flooding spreads beyond exact coordinates.

📊 Flood Risk Scoring (Explainable)

Flood Risk Score (0–100) is computed using:

Risk Score =
  Terrain Deficit (Elevation)
+ Climate Stress (Extreme Rainfall)
+ Flood Memory Severity


Each component is explainable, visible to the user, and auditable.

No black-box ML is used for scoring.

🔍 Key Features

📍 Address Search with Auto-Centering

🖱️ Click-Anywhere Point Analysis

🧠 “Flood Memory” with Year-Specific Events

🧭 Buyer / Engineer Mode Separation

🧱 Blueprint Upload (Engineer Mode Only)

🧾 AI-Generated Impact Narratives

🧠 Agent Architecture Transparency

📘 Step-by-Step User Guide (In-App)

🧪 Tech Stack

Frontend / App: Streamlit

Maps: Folium + OpenStreetMap + Esri + OpenTopoMap

Geocoding: Nominatim (OpenStreetMap)

Climate & Elevation Data: Open-Meteo + NASA SRTM

AI Reasoning: Google Gemini (text-only, grounded)

Hosting: Streamlit Community Cloud (free tier)

🚀 Running the App Locally
pip install streamlit streamlit-folium folium geopy requests google-generativeai
streamlit run app.py


Set your Gemini API key in .streamlit/secrets.toml:

GEMINI_API_KEY = "your_api_key_here"

⚠️ Limitations (Explicit & Honest)

Flood memory is prototype-level, not exhaustive

No real-time drainage sensor integration (yet)

Climate projection is trend-based, not simulation-based

Not a replacement for certified civil engineering approval

These limitations are clearly communicated in the UI.

🔮 Future Scope

Ward-wise flood memory expansion via automated news ingestion

Two-location comparison (e.g., “Which flat is safer?”)

PDF exportable risk reports

Integration with municipal drainage datasets

Climate scenario slider (2030 / 2040 / 2050)

🏆 Why Neev AI Is Impactful

Moves flood assessment from maps → decisions

Makes hidden urban risks visible and explainable

Bridges data science, civil engineering, and AI

Designed for real people, not just planners

📜 License

Prototype / Hackathon use only.
Data sources are public and attribution-compliant.
