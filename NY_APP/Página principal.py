import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode



st.set_page_config(page_title="NEWYORK DASHBOARD",
                   page_icon=":bar_chart:",
                   layout="wide"
)


st.markdown("<h1 style='text-align: center; color: grey;'>NEW YORK APP</h1>", unsafe_allow_html=True)

st.write(""" # Se ha realizado un estudio de la Data de
Airbnb correspondiente al año 2011 al 2019
en la cual consta de 48,895 registros de la
Ciudad de New York.""")




#st.sidebar.header("Please Filter Here by :")

#Neigborhood = st.sidebar.multiselect(
#               "select de borough",
#                options = df['neighbourhood_group'].unique()
#               )




















