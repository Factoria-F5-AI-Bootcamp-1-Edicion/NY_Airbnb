import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Multipage App"
)


image = Image.open('logo2.png')

st.image(image, caption='')

st.write(""" ### Somos una startup conformado de 4 emprendedores, Jonathan: encargado de diseño de páginas web y apps, Felix: Ingeniero en Programacióon, Henry: Especialista en Análisis de datos y Celeste: Coordinadora de Marketing y nos dedicados a la consultoria y estatregia de ventas para empresas turisticas. 

### Usando nuestro innovador algoritmo de inteligencia artificial, medimos detalladamente los  patrones en el análisis de datos para mejorar el rendimiento y aumentar la rentabilidad de tu proyecto turístico. 
 
### Nuestra herramienta te ayudará a poder impulsar tu empresa al próximo nivel. Para más información, escribenos a nuestro correo electrónico para agendar una análisis inicial.

""")

