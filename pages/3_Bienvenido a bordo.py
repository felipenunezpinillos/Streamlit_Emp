import streamlit as st

from streamlit_extras.switch_page_button import switch_page

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
    st.title("Bienvenido a bordo")

st.subheader("A continuación te pediremos información del emprendimiento que nos ayudará a hacer nuestro trabajo")

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

# Insert a clickable submit button that spans the width of the page
button_clicked = st.button("Empezar ->", key="submit_button")

# Perform actions when the button is clicked
if button_clicked:
    switch_page("Que buscas con nosotros")

