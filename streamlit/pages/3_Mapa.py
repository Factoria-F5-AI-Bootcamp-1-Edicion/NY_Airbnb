import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk





def data_upload():
    df = pd.read_csv('NY_airbnb.csv')
    return df
df = data_upload()



df = pd.DataFrame(
     np.random.randn(100, 2) / [50, 50] + [40.6643, -73.9385],
     columns=['latitude', 'longitude'])

st.map(df)