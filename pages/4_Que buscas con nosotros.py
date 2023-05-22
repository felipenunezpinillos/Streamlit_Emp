import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Crea dos botones dentro de un contenedor centrado horizontalmente
container = st.container()

# Crea dos columnas para la imagen y el texto
col1, col2 = st.columns([1, 2])

# Inserta una imagen en la primera columna
col1.image("images/nexus_logo.jpeg", width=100)

# Inserta texto en la segunda columna
col2.title("¿Qué buscas con nosotros?")

# Define el estilo CSS para centrar los botones y establecer el tamaño
# Add custom CSS for dark mode and button styling
custom_css = """
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
st.markdown(custom_css, unsafe_allow_html=True)

#Botones
boton1 = st.button("Busco nuevos emprendimientos", key="submit_button1")
boton2 = st.button("Tengo un nuevo emprendimiento", key="submit_button2")

if boton1:
    switch_page("Sobre el Buscador")
    
if boton2:
    switch_page("Sobre tu emprendimiento")