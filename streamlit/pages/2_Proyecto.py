from ast import main
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

st.markdown("<h1 style='text-align: center; color: darkblue;'>Análisis de la oferta de vivienda vacacional en NYC</h1>", unsafe_allow_html=True)



st.write(""" ### El análisis está orientado a demostrar las potencialidades de inversión existentes en los actuales momentos en el sector inmobiliario de NYC con el objeto de ampliar la oferta de alojamiento en la medida en que aumenta la demanda  por este tipo de alternativa. 
### En 2019, previo a la pandemia, 65 millones de turistas visitaron la ciudad. Se estima que el presente año alcance los 56 millones, aunque alejada de la cifra prepandemia se nota una rápida recuperación.
### El Análisis Exploratorio de Datos corespondiente a Airbnb NY entre el año 2011 al 2019 arroja una disponibilidad de 48,895 alojamientos, correspondientes al total de registros existentes.
""")

st.write(""" ### La data está referida a los 5 Distritos que conforman la Ciudad de NY:
### - Bronx             
### - Brooklyn         
### - Manhattan        
### - Queens            
### - Staten Island

### e incluye un total de 221 vecindarios 

""")


#comienza tabla con filtros
@st.cache 
def data_upload():
    df = pd.read_csv('NY_airbnb.csv')
    return df

df = data_upload()

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)

gd.configure_side_bar()

gd.configure_selection(selection_mode='multiple',use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(df,gridOptions=gridoptions,
                    update_mode= GridUpdateMode.SELECTION_CHANGED,
                    height = 500,
                    allow_unsafe_jscode=True,
                    theme='balham') #theme error con blue, lo cambie por balham, cuando da error te dicde cuales puedes usar

sel_row = grid_table["selected_rows"]
st.sidebar.dataframe(sel_row)
#termina tabla 



#grafica1 ACA NO LE PUDE PONER TITULO A LA GRAFICA

st.write(""" #### Se realizo un grafico de Barras y observamos que el Distrito mas caro para alquiler es Manhattan y Brooklyn
""")

st.write(""" 
""")

st.bar_chart((df['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count")



#grafica2
st.write("""

""")#se creo para dejar espacio entre graficas

plt.scatter(df["price"],df["neighbourhood_group"])
plt.title("PENDIENTE PONERLE TITULO")

st.set_option('deprecation.showPyplotGlobalUse', False) 

fig = st.pyplot()


#grafica3

st.write(""" 

""")#este st.write lo puse solo para que me deje espacio entre graficas 

df['neighbourhood'].value_counts()[:15].plot(kind='bar')
plt.title("Vecindarios más demandados")
fig = st.pyplot()


st.write(""" ### De los cuatro principales  propietarios , los dos primeros representan a startup

### - Sonder =  327 
### - Blueground = 232
### - kara = 121
### - kazuya = 103

### No obstante, el 66,06% de la oferta total pertenece a propietarios individuales (32.303)

""")
#termina grafica

st.write("""

""")

st.markdown("<h1 style='text-align: center; color: darkblue;'>Variables estadisticas del precio y tipo de alojamientos por Distritos</h1>", unsafe_allow_html=True)



group1 = df.groupby(['neighbourhood_group', 'room_type'])['price'].agg(['count', 'min', 'max', 'mean' ,'median', 'std'])

group1



st.write(""" ### La oferta de alojamiento se distribuye de la siguiente manera:

### - Entire home/apt = 25409
### - Private room    = 22326
### - Shared room     = 1160 

""")