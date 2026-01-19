# 🌊 Neev AI — Urban Flood Intelligence & Decidability System

Neev AI is an **urban flood-risk decision intelligence platform** designed for flood-prone Indian cities, with a pilot deployment focused on **Guwahati, Assam**.

Unlike traditional flood maps that mark only a few red zones, Neev AI answers a harder and more practical question:

> **“Has this exact place flooded before, why did it flood, how severe was it, and what is likely to happen in the future?”**

The system is built for **buyers, renters, engineers, planners, and policymakers** who need **street-level clarity**, not district-level averages.

---

## 🚨 Problem Statement

Urban flooding in Indian cities suffers from four structural problems:

1. **Extreme localization**  
   Flooding often affects one street while the next street remains dry.

2. **Loss of institutional memory**  
   Past flood events are scattered across news articles, municipal notices, and social reports — not structured datasets.

3. **Static flood maps**  
   Existing maps show fixed zones and fail to capture recurrence, propagation, or micro-terrain effects.

4. **No explainability**  
   Most tools label an area as “safe/unsafe” without explaining *why*.

As a result, people make **high-stakes real-estate and construction decisions blindly**.

---

## 💡 Neev AI — Core Idea

Neev AI treats flooding as a **decidable phenomenon**, not a binary label.

Each location is evaluated using:
- Physical terrain constraints
- Multi-year rainfall recurrence
- Verified historical flood memory
- Distance-based impact propagation
- AI-generated human-readable explanations

This allows risk assessment **even if the exact coordinate was never officially mapped as flooded**.

---

## 👥 Who Is This For?

### 🏠 Buyers & Renters
- “Did this exact street flood in 2022?”
- “What kind of damage usually happens here?”
- “Will parking or ground floors be affected?”

### 👷 Engineers & Builders
- “Is this site a drainage bowl?”
- “Should basements be avoided?”
- “What mitigation strategies are required?”

---

## 🧠 System Architecture (Agentic Design)

Neev AI is implemented as a **multi-agent decision system** where each agent has a clearly defined epistemic role.

---

### **Agent A — Physics (Deterministic)**  
**What it does**
- Queries satellite-derived Digital Elevation Models (DEM)
- Detects low-lying terrain and drainage constraints

**Why deterministic**
- Elevation must be factual
- No AI hallucination allowed

---

### **Agent B — Climate Recurrence (Deterministic)**  
**What it does**
- Scans **2020–2024 monsoon seasons**
- Counts extreme rainfall days (>50mm/day)
- Captures recurrence, not one-off events

**Why multi-year**
- Prevents “last year was a fluke” errors

---

### **Agent B2 — Flood Memory (Knowledge-Grounded)**  
**What it does**
- Maintains a structured **Flood Memory Database**
- Built from:
  - News reports
  - Municipal disclosures
  - Resident-reported events

**Stored attributes**
- Ward
- Affected radius (flood spreads, not points)
- Flood years
- Impact descriptions
- Severity score

**Enables statements like**
> **“This exact street flooded in 2022.”**

---

### **Agent C — AI Consultant (Gemini)**  
**What it does**
- Does *not* compute risk scores
- Converts structured signals into:
  - Damage narratives
  - Resident experience explanations
  - 2035 climate outlook

**Key constraint**
- AI reasoning is **grounded only on Agent A/B/B2 outputs**

---

## 🗺️ Mapping & Visualization

Neev AI provides **multi-layer GIS intelligence**, not a single map.

### Available Layers
- 🛣️ Street Map (navigation & locality context)
- 🛰️ Satellite Imagery (built-up area & drainage clues)
- ⛰️ Elevation / Topographic Map (slope & basin awareness)
- 🌊 Flood Memory Zones (historical impact areas)

Flood areas are intentionally modeled as **zones**, because real flooding spreads to surrounding streets.

---

## 📊 Flood Risk Scoring (Explainable)

The Flood Risk Score (0–100) is computed using:
-Risk Score =
T-errain Deficit (Elevation)
-Climate Stress (Extreme Rainfall)

Flood Memory Severity

There is **no black-box ML** in scoring.  
Every component is visible and explainable in the UI.

---

## 🔍 Key Features

- 📍 Address search with auto-centering
- 🖱️ Click-anywhere point analysis
- 🧠 “Flood Memory” with year-specific events
- 🧭 Buyer vs Engineer mode separation
- 🧱 Blueprint upload (Engineer mode only)
- 🧾 AI-generated impact narratives
- 🗺️ Multiple map layers (Street / Satellite / Elevation)
- 📘 In-app step-by-step user guidance
- 🧠 Transparent agent architecture explanation

---

## 🧪 Tech Stack

- **App Framework**: Streamlit  
- **Maps & GIS**: Folium, OpenStreetMap, Esri World Imagery, OpenTopoMap  
- **Geocoding**: Nominatim (OpenStreetMap)  
- **Climate & Elevation Data**: Open-Meteo, NASA SRTM  
- **AI Reasoning**: Google Gemini (text-only, grounded)  
- **Hosting**: Streamlit Community Cloud  

---

## 🚀 Running the App Locally

```bash
pip install streamlit streamlit-folium folium geopy requests google-generativeai
streamlit run app.py
