import streamlit as st

# Create two columns: one for the image and one for the text
col1, col2 = st.columns([1, 2])

# Inserting an image with custom size and alignment
st.markdown(
    """
    <style>
    .small-image {
        width: 100px;
        height: auto;
        object-fit: contain;
        float: left;
        margin-right: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Insert the image in the first column
with col1:
    st.image("images/nexus_logo.jpeg", width=100)

# Insert the text in the second column
with col2:
    st.title("Registrarse")

st.subheader("Cuentanos un poco sobre ti")

with st.form(key='form1'):
    nombre = st.text_input("Nombre")

    apellido = st.text_input("Apellido")

    email = st.text_input("Email")

    ctr = st.text_input("Contraseña", type = 'password')

    r_ctr = st.text_input("Confirma tu contraseña", type = 'password')

    submit_button = st.form_submit_button(label = 'Crear cuenta')

if submit_button and nombre != "" and apellido != "" and email != "" and ctr != "" and r_ctr != "":
        if submit_button and ctr == r_ctr:
            st.success("¡Felicidades {} {} ya haces parte de la familia Nexus!".format(nombre, apellido))
            st.success("Bienvenido de nuevo")
            switch_page("Dashboard")

        elif submit_button and ctr != r_ctr: 
            st.error("Las contraseñas no coinciden")


elif submit_button and nombre == "" and apellido == "" and email == "" and ctr == "" and r_ctr == "": 
    st.error("Ingresa valores validos")
