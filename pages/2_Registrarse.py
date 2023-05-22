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
