import streamlit as st
from streamlit_ace import st_ace
import base64
from streamlit_extras.switch_page_button import switch_page

st.title("Sobre tu emprendimiento!")
st. subheader("Logo")
# Crea dos columnas, una para el widget st_ace y otra para la imagen de perfil
col1, col2 = st.columns([1, 1])

# Widget de texto
st. subheader("Nombre")
nombre = st.text_input("Ingresa el nombre de tu emprendimiento")

# Widget de selección de color
st. subheader("Color principal")
color = st.color_picker("Selecciona el color principal de tu emprendimiento", "#FF0000")

st. subheader("Color secundario")
color2 = st.color_picker("Selecciona el color secundario de tu emprendimiento", "#FF0000")

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
boton1 = st.button("Siguiente", key="submit_button")

if boton1 and nombre != "":
        switch_page("Oferta de productos y servicios emprendimiento")
elif boton1 and nombre == "":
    st.error("Ingresa el nombre de tu emprendimiento")

# Utiliza st_ace en la primera columna para crear el elemento de carga de archivos
uploaded_code = col1.container()

uploaded_file = uploaded_code.file_uploader("Añade el logo de tu emprendimiento", type=['png', 'jpeg', 'jpg'], key="uploaded_file")

# Verifica si se ha cargado un archivo y muestra la imagen de perfil en la segunda columna
if uploaded_file is not None:
    # Lee los datos de la imagen cargada
    img_bytes = uploaded_file.read()

    # Convierte los datos de la imagen a formato base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    # Muestra la imagen de perfil con estilo convencional utilizando HTML en la segunda columna
    col2.markdown(
        f'<style>.profile-pic {{ width: 150px; height: 150px; border-radius: 50%; object-fit: cover; }}</style>',
        unsafe_allow_html=True
    )
    col2.markdown(f'<img class="profile-pic" src="data:image/png;base64,{img_base64}" alt="Foto de perfil">',
                unsafe_allow_html=True)