#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 22:01:57 2025

@author: abheekpathirana
"""

import streamlit as st
import pandas as pd

# === Page configuration ===
st.set_page_config(
    page_title="Barn Buddy - Farmer Locations",
    page_icon="🌱",
    layout="wide",
)

# === Custom CSS for green theme ===
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
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Sidebar ===
st.sidebar.header("Barn Buddy 🌿")
st.sidebar.markdown("""
Welcome to **Barn Buddy**, Our farm locations dashboard.  
Navigate below:
- Farmer locations in Nuwara Eliya
- Our HQ
""")

cities = pd.DataFrame({
    'city': ['Barn buddy HQ'],
    'lat': [6.9675],
    'lon': [80.7800]
})


# === Major Sri Lankan cities ===


st.subheader("Our Location")
st.map(cities, zoom=14)

# === Nuwara Eliya farmer points ===
nuwara_eliya_points = pd.DataFrame({
    "lat": [
        6.9701, 6.9672, 6.9743, 6.9725, 6.9658,
        6.9804, 6.9782, 6.9629, 6.9757, 6.9688
    ],
    "lon": [
        80.7828, 80.7740, 80.7765, 80.7812, 80.7804,
        80.7865, 80.7890, 80.7952, 80.7800, 80.7815
    ]
})

st.subheader("Nuwara Eliya Farmer Locations 🌱")
st.map(nuwara_eliya_points, zoom=13)

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