import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Barn Buddy - Farmer Locations", page_icon="🌱", layout="wide")

# Custom CSS
st.markdown("""
<style>
.stApp { background-color: #f0fff4; }
.css-18e3th9 { color: #1b5e20; font-size: 48px; font-weight: bold; }
.stBlock { background-color: #e8f5e9; border-radius: 15px; padding: 20px; margin-bottom: 25px; box-shadow: 0 8px 25px -5px rgba(46,125,50,0.4); }
div.stButton > button { background-color: #2e7d32; color:white; font-size:18px; border-radius:8px; padding:8px 20px; margin-top:15px; transition:all 0.3s ease; }
div.stButton > button:hover { background-color:#1b5e20; transform: scale(1.05); }
</style>
""", unsafe_allow_html=True)

st.subheader("🌱 Farmer Locations in Nuwara Eliya")

# === Leaflet HTML map ===
map_html = """
<div id="map" style="width: 100%; height: 600px;"></div>
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
var map = L.map('map').setView([6.970231, 80.782912], 13);

// OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(map);

// HQ marker
L.marker([6.970231, 80.782912]).addTo(map)
    .bindPopup('🏠 Barn Buddy collection point')
    .openPopup();

// Farmer markers
var farmers = [
  [6.9609845,80.7765321,"Kandapola – carrot & potato belt"],
  [6.9707345,80.7676321,"Kandapola–Pedro stretch, tea + veg"],
  [6.9804845,80.7587321,"Pedro side – high-elevation carrots"],
  [6.9902345,80.7498321,"Horton Plains road – strawberry zone"],
  [6.9009845,80.7811321,"Ambewela – large-scale strawberries"],
  [6.9107345,80.7722321,"Ambewela south – mixed crops"],
  [6.9204845,80.7633321,"Near New Zealand Farm – pasture/veg"],
  [6.9302345,80.7544321,"Seetha Eliya–Ambewela route – veg band"],
  [6.9409845,80.7455321,"Between Ambewela & Pattipola – cool-climate belt"]
];

farmers.forEach(function(f) {
  L.circleMarker([f[0], f[1]], {radius:6, color:'#2e7d32', fillColor:'#66bb6a', fillOpacity:0.8})
   .bindTooltip(f[2])
   .addTo(map);
});
</script>
"""

components.html(map_html, height=600, scrolling=False)

if st.button("🌍 Visit Barn Buddy Website"):
    st.markdown("[Click here to open Barn Buddy](https://barn-buddy-demo.lovable.app)", unsafe_allow_html=True)
