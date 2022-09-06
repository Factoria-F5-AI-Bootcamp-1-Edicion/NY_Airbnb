import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from streamlit_folium import folium_static
import folium



st.title("CONTACTANOS")



mapa = folium.Map(location=[40.71427, -74.00597], zoom_start=11)

tooltip = "Statue of Liberty"
folium.Marker(
         [40.689249, -74.044500], popup="Statue of Liberty", tooltip=tooltip
    ).add_to(mapa)

    # call to render Folium map in Streamli
folium_static(mapa)