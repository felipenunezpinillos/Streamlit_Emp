import streamlit as st
from streamlit_ace import st_ace
import base64
from streamlit_extras.switch_page_button import switch_page

st.title("¿Qué tipo de productos ofreces?")

st. subheader("Buscar categorías de tus productos por nombre")

# Opciones de categorías
categorias_productos = [
    "Tecnología",
    "Deportes",
    "Arte y cultura",
    "Moda",
    "Viajes",
    "Ninguno",
]

categorias_servicios = [
    "Tecnología",
    "Deportes",
    "Arte y cultura",
    "Moda",
    "Viajes",
    "Ninguno",
]
# Widget de checklist
categorias_seleccionadas = st.multiselect("Selecciona las categorias de tus productos", categorias_productos, key='mt1')

# Add custom CSS for dark mode and button styling
custom_css1 = """
<style>
body {
    background-color: #222222;
    color: #ffffff;
}

.stButton button {
    display: block;
    width: 100%;
    margin: 0 auto;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css1, unsafe_allow_html=True)

st. subheader("Buscar categorías de tus servicios por nombre")

# Widget de checklist
categorias_seleccionadas = st.multiselect("Selecciona las categorias de tus servicios", categorias_servicios, key='mt2')

# Add custom CSS for dark mode and button styling
custom_css2 = """
<style>
body {
    background-color: #222222;
    color: #ffffff;
}

.stButton button {
    display: block;
    width: 100%;
    margin: 0 auto;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css2, unsafe_allow_html=True)

#Botones
boton = st.button("Siguiente", key="submit_button")
if boton:
    switch_page("imagenes emprendimiento")
    

