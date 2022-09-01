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
plt.title("Precios por Distritos")

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


st.markdown("<h1 style='text-align: center; color: darkblue;'>Conclusione</h1>", unsafe_allow_html=True)


st.write(""" ### La mayor concentracion de la oferta de alojamiento vacacional, se ubican en Manhttan y Brooklyn, Distritos en los que se concentran  las principales atracciones turisticas, una amplia oferta comercial 24/7, y atención de seguridad. 
### Dentro de los Distritos de Manhattan y Brooklyn, se ubican los 14 vencindarios con mayor oferta de alojamiento

### - Williamsburg = 3920
### - Bedford-Stuyvesant = 3714
### - Harlem = 2658
### - Bushwick = 2465
### - Upper West Side = 1971
### - Hell's Kitchen = 1958
### - East Village = 1853
### - Upper East Side = 1798
### - Crown Heights = 1564
### - Midtown = 1545
### - East Harlem = 1117
### - Greenpoint = 1115
### - Chelsea = 1113
### - Lower East Side = 911
### - Astoria = 900

""")

st.write(""" ### Los principales propietarios tienen mas de 100 alojamientos para alquilar, siendo el principal El Host ID 219517861.

""")


st.write(""" ### La principal oferta de alojamiento son casas o apartamentos completos = 25,409 total seguidos por habitaciones privadas 22,326 y ultima instancia cuartos compartidos 1,160

""")

st.write(""" Los mayores costos de alquiler, se ubican en el distrito de Manhattan, seguidos por Brooklyn y el mas economico en el Bronx. 
El precio está relacionado con la ubicación del alojamiento y los servicios y atracciones disponibles.
  El Bronx es uno de los Distritos más deprimidos de la Ciudad de New York. Históricamente, la zona ha sido asociada a la pobreza,  violencia, drogas y crimen. aunque algunas áreas han visto un mejoramiento urbanístico debido a los procesos de rezonificación.
La pandemia de COVID-19 impactó negtivamente al turismo  y la rentabilidad correspondiente. Sin embargo, desde el año 2021 se ha observado una mejoría en el sector.  



""")


st.write (""" ### Precios actuales en el trimestre | Precio medio por pie cuadrado | Precio medio de venta
 --- | --- | ---
**Coops** | **$1,139** | **$1.28M** |
**Condominios** | **$1,921** | **$2.64M**
**Nuevo desarrollo**| **$2,581** | **$3.84M**  
**Lujo (10% superior)**| **$2,636** | **$7.75M**

""")