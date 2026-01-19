# 🌊 Neev AI – Urban Flood Intelligence System

**Neev AI** is an urban flood-risk decision intelligence platform designed for flood-prone Indian cities, with a pilot focus on **Guwahati, Assam**.

Unlike traditional flood maps that rely on static zones, Neev AI combines **terrain physics**, **multi-year climate recurrence**, **verified flood memory**, and **AI-assisted interpretation** to answer one critical question:

> **“Has this exact place flooded before, why did it flood, and what is likely to happen in the future?”**

---

## 🚨 Problem Statement

Urban flooding in Indian cities is:
- **Highly localized** (street-level, not district-level)
- **Poorly documented** in official maps
- **Underestimated** by buyers, renters, and even engineers
- **Increasingly severe** due to climate change and urbanization

Most existing solutions fail because they:
- Use **static flood zones**
- Ignore **historical news-verified flooding**
- Provide **no explanation or context**
- Are unusable for **non-technical users**

---

## 💡 Neev AI – Core Idea

Neev AI treats flooding as a **decidable phenomenon**, not a binary label.

Every location is evaluated using:
- **Physical terrain constraints**
- **Multi-year rainfall stress**
- **Historical flood memory**
- **Proximity-based impact propagation**
- **Human-readable AI explanations**

This enables risk assessment **even if the exact coordinate was never officially mapped**.

---

## 👥 Target Users

### 🏠 Buyers / Renters
- “Did this exact street flood in the past?”
- “Will my parking or ground floor be affected?”
- “Is this risk occasional or chronic?”

### 👷 Engineers / Builders
- “Is this site a drainage bowl?”
- “Should basements be avoided here?”
- “What mitigation strategies are required?”

---

## 🧠 System Architecture (Agentic Design)

Neev AI is built as a **multi-agent decision system**.

### **Agent A – Physics (Deterministic)**
- Uses satellite-derived DEM (Digital Elevation Model)
- Identifies low-lying terrain and drainage constraints
- No AI hallucination — hard numbers only

### **Agent B – Climate Recurrence (Deterministic)**
- Scans **2020–2024 monsoon data**
- Counts extreme rainfall events (>50mm/day)
- Captures recurrence, not single-year anomalies

### **Agent B2 – Flood Memory (Knowledge-Grounded)**
- Structured database built from:
  - News reports
  - Municipal disclosures
  - Resident-reported flooding
- Stores:
  - Affected ward
  - Flood years
  - Severity
  - Impact radius
- Enables statements like:
  > **“This exact street flooded in 2022.”**

### **Agent C – AI Consultant (Gemini)**
- Does **not** compute scores
- Converts structured risk signals into:
  - Damage narratives
  - Resident impact explanations
  - 2035 climate outlook
- Fully grounded on Agent A/B/B2 outputs

---

## 🗺️ Mapping & Visualization

Neev AI provides **multi-layer GIS intelligence**:

- **Street Map** – locality & navigation context  
- **Satellite Map** – built-up area & drainage patterns  
- **Elevation (Topo) Map** – terrain & slope awareness  
- **Flood Memory Overlays** – historical impact zones  

Flood areas are intentionally modeled as **zones**, not points, because real flooding spreads beyond exact coordinates.

---

## 📊 Flood Risk Scoring (Explainable)

Flood Risk Score (0–100) is computed using:

