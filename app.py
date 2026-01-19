import streamlit as st
from streamlit_folium import st_folium
import folium
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import google.generativeai as genai
import json

# =========================================================
# APP CONFIG
# =========================================================

st.set_page_config(
    page_title="Neev AI | Urban Flood Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# MODERN UI STYLING
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #0f172a;
}

.stContainer {
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    background: #ffffff;
}

.section-card {
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: #f8fafc;
    margin-bottom: 16px;
}

.verdict {
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-weight: 600;
}

.high { background: #fee2e2; color: #7f1d1d; }
.mid  { background: #fff7ed; color: #9a3412; }
.low  { background: #ecfeff; color: #155e75; }

.caption {
    font-size: 0.85rem;
    color: #64748b;
}

button {
    border-radius: 10px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# GEMINI CONFIG
# =========================================================

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    GEMINI_ENABLED = True
except:
    GEMINI_ENABLED = False

# =========================================================
# FLOOD MEMORY DATABASE (AGENT B2)
# =========================================================


FLOOD_MEMORY = {
    "Anil Nagar": {
        "ward": "Ward 42",
        "lat": 26.1685,
        "lon": 91.7760,
        "radius": 900,
        "flood_types": ["Urban Drainage Failure", "Pluvial Flooding"],
        "severity": 5,
        "events": {
            2017: "Ground floor homes flooded",
            2020: "Sewage backflow reported",
            2022: "Vehicles stalled overnight",
            2024: "Flash flooding within 30 minutes of rainfall"
        }
    },
    "Hatigaon": {
        "ward": "Ward 57",
        "lat": 26.1515,
        "lon": 91.7955,
        "radius": 800,
        "flood_types": ["Urban Drainage Failure"],
        "severity": 4,
        "events": {
            2019: "Residential colonies waterlogged",
            2022: "Repeated road submergence"
        }
    },
    "Rukminigaon": {
        "ward": "Ward 58",
        "lat": 26.1350,
        "lon": 91.7850,
        "radius": 1000,
        "flood_types": ["Seasonal Waterlogging"],
        "severity": 4,
        "events": {
            2020: "Traffic paralysis",
            2023: "Basement parking flooded"
        }
    },
    "Ganeshguri": {
        "ward": "Ward 44",
        "lat": 26.1610,
        "lon": 91.7840,
        "radius": 700,
        "flood_types": ["Flash Flooding"],
        "severity": 3,
        "events": {
            2018: "Commercial disruption",
            2024: "Short duration flash flood"
        }
    }
}

# =========================================================
# AGENTS
# =========================================================

def get_elevation(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}"
        return requests.get(url, timeout=3).json()["elevation"][0]
    except:
        return 50.0

def rainfall_events(lat, lon):
    try:
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": "2020-06-01",
            "end_date": "2024-09-30",
            "daily": "rain_sum"
        }
        data = requests.get(url, params=params, timeout=5).json()
        return sum(1 for r in data["daily"]["rain_sum"] if r and r > 50)
    except:
        return 0

def match_flood_memory(lat, lon):
    hits = []
    for area, info in FLOOD_MEMORY.items():
        d = geodesic((lat, lon), (info["lat"], info["lon"])).meters
        if d <= info["radius"]:
            hits.append((area, info, int(d)))
    return hits

def generate_narrative(score, memory_hits):
    if not GEMINI_ENABLED:
        return "AI narrative unavailable."

    model = genai.GenerativeModel("gemini-1.0-pro")
    context = ", ".join([f"{a} flooded in {list(i['events'].keys())}" for a,i,_ in memory_hits])

    prompt = f"""
You are an urban flood risk analyst in Guwahati.

Risk Score: {score}/100
Historical context: {context}

Explain likely damage, resident impact, and 2035 outlook.
"""
    return model.generate_content(prompt).text

# =========================================================
# MAP
# =========================================================

def render_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=14, tiles=None)

    folium.TileLayer("OpenStreetMap", name="Street").add_to(m)
    folium.TileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri", name="Satellite"
    ).add_to(m)
    folium.TileLayer(
        "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        attr="Topo", name="Elevation"
    ).add_to(m)

    for area, info in FLOOD_MEMORY.items():
        folium.Circle(
            [info["lat"], info["lon"]],
            radius=info["radius"],
            color="#dc2626",
            fill=True,
            fill_opacity=0.12,
            tooltip=f"{area} flooded in {', '.join(map(str, info['events'].keys()))}"
        ).add_to(m)

    folium.Marker([lat, lon], icon=folium.Icon(icon="info-sign")).add_to(m)
    folium.LayerControl().add_to(m)

    return st_folium(m, height=520, width="100%", returned_objects=["last_clicked"])

# =========================================================
# PAGES
# =========================================================

def page_home():
    st.title("🌊 Neev AI")
    st.subheader("Urban Flood Intelligence for Safer Decisions")

    st.markdown("""
    **Neev AI** helps residents, buyers, and engineers understand **real flood risk**  
    — not just elevation, but **what actually flooded, where, and why**.

    Built specifically for **Guwahati**, using:
    - Historical flood memory
    - Terrain physics
    - Climate recurrence
    - AI-assisted interpretation
    """)

def page_intelligence():
    if "lat" not in st.session_state:
        st.session_state.lat = 26.1685
        st.session_state.lon = 91.7760

    mode = st.radio("User Mode", ["Buyer / Renter", "Engineer"], horizontal=True)

    search = st.text_input("Search address (auto-centers map)")
    if search:
        loc = Nominatim(user_agent="neev_ai").geocode(search)
        if loc:
            st.session_state.lat, st.session_state.lon = loc.latitude, loc.longitude

    col1, col2 = st.columns([1.6, 1])

    with col1:
        map_data = render_map(st.session_state.lat, st.session_state.lon)
        if map_data and map_data.get("last_clicked"):
            st.session_state.lat = map_data["last_clicked"]["lat"]
            st.session_state.lon = map_data["last_clicked"]["lng"]

    with col2:
        elev = get_elevation(st.session_state.lat, st.session_state.lon)
        rain = rainfall_events(st.session_state.lat, st.session_state.lon)
        memory_hits = match_flood_memory(st.session_state.lat, st.session_state.lon)

        memory_score = max([i["severity"] for _,i,_ in memory_hits], default=0)
        score = min(int((50 - elev) * 2 + rain * 2 + memory_score * 10), 100)

        cls = "high" if score > 60 else "mid" if score > 30 else "low"
        st.markdown(f"<div class='verdict {cls}'>Flood Risk Score: {score}/100</div>", unsafe_allow_html=True)

        st.markdown("### 🧠 Flood Memory")
        for area, info, dist in memory_hits:
            st.markdown(f"- **{area}** ({dist} m): flooded in {', '.join(map(str, info['events'].keys()))}")

        if mode == "Engineer":
            st.file_uploader("Upload design drawings")

        if st.button("Generate Impact Narrative"):
            st.write(generate_narrative(score, memory_hits))

def page_agents():
    st.title("🧠 Agentic System")

    st.markdown("""
    **Agent A – Physics**
    - Satellite elevation (DEM)
    
    **Agent B – Climate**
    - 5-year extreme rainfall recurrence
    
    **Agent B2 – Flood Memory**
    - Verified historical flood events by ward
    
    **Agent C – AI Consultant**
    - Interprets risk & explains human impact
    """)

def page_guide():
    st.title("📘 How to Use Neev AI")

    st.markdown("""
    **Step 1:** Search your address or click on the map  
    **Step 2:** View flood memory & risk score  
    **Step 3:** Switch modes (Buyer / Engineer)  
    **Step 4:** Generate impact narrative  

    *No blueprints required for buyers.*
    """)

# =========================================================
# MAIN
# =========================================================

def main():
    with st.sidebar:
        st.markdown("## Neev AI")
        page = st.radio("Navigation", ["🏠 Home", "🗺️ Flood Intelligence", "🧠 Agentic System", "📘 How to Use"])

    if page == "🏠 Home": page_home()
    if page == "🗺️ Flood Intelligence": page_intelligence()
    if page == "🧠 Agentic System": page_agents()
    if page == "📘 How to Use": page_guide()

if __name__ == "__main__":
    main()

