import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# === Page configuration ===
st.set_page_config(
    page_title="Barn Buddy - Farmer Locations",
    page_icon="🌱",
    layout="wide"
)

# === Custom CSS for premium green aesthetic ===
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #f0fff4;
    }
    /* Title styling */
    .css-18e3th9 {
        color: #1b5e20;
        font-size: 48px;
        font-weight: bold;
    }
    /* Card/Container styling */
    .stBlock {
        background-color: #e8f5e9;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px -5px rgba(46, 125, 50, 0.4);
    }
    /* Button styling */
    div.stButton > button {
        background-color: #2e7d32;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 8px 20px;
        margin-top: 15px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #1b5e20;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Sidebar ===
st.sidebar.header("Barn Buddy 🌿")
st.sidebar.markdown("""
Welcome to **Barn Buddy**, your smart farm dashboard.  
Navigate below:
- Farmer locations in Nuwara Eliya
- Our collection point
""")

# === Farmer locations (static) ===
nuwara_eliya_points = pd.DataFrame({
    "lat": [
        6.9609845, 6.9707345, 6.9804845, 6.9902345, 6.9009845,
        6.9107345, 6.9204845, 6.9302345, 6.9409845
    ],
    "lon": [
        80.7765321, 80.7676321, 80.7587321, 80.7498321, 80.7811321,
        80.7722321, 80.7633321, 80.7544321, 80.7455321
    ],
    "tooltip": [
        "Kandapola – carrot & potato belt",
        "Kandapola–Pedro stretch, tea + veg",
        "Pedro side – high-elevation carrots",
        "Horton Plains road – strawberry zone",
        "Ambewela – large-scale strawberries",
        "Ambewela south – mixed crops",
        "Near New Zealand Farm – pasture/veg",
        "Seetha Eliya–Ambewela route – veg band",
        "Between Ambewela & Pattipola – cool-climate belt"
    ]
})

# === HQ location ===
hq_lat, hq_lon = 6.970231, 80.782912

# === Create Folium map ===
m = folium.Map(location=[hq_lat, hq_lon], zoom_start=13, tiles="OpenStreetMap")
# HQ marker
folium.Marker(
    [hq_lat, hq_lon],
    popup="Barn Buddy HQ",
    tooltip="🏠 Barn Buddy collection point",
    icon=folium.Icon(color="green", icon="home")
).add_to(m)
# Farmer markers
for _, row in nuwara_eliya_points.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=6,
        color="#2e7d32",
        fill=True,
        fill_color="#66bb6a",
        fill_opacity=0.8,
        tooltip=row["tooltip"]
    ).add_to(m)

# === Display map in styled card ===
st.markdown('<div class="stBlock">', unsafe_allow_html=True)
st.subheader("🌱 Farmer Locations in Nuwara Eliya")
st_folium(m, width=900, height=600)
st.markdown('</div>', unsafe_allow_html=True)

# === Visit website button ===
if st.button("🌍 Visit Barn Buddy Website"):
    st.markdown("[Click here to open Barn Buddy](https://barn-buddy-demo.lovable.app)", unsafe_allow_html=True)

# === Footer ===
st.markdown(
    """
    <hr>
    <p style='text-align:center;color:#1b5e20;font-size:14px'>
    © 2025 Barn Buddy. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)
