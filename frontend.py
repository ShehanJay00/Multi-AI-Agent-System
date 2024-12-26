import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="MovieMate - Your Movie Companion", layout="wide")

# Inject custom CSS for hover effects
st.markdown(
    """
    <style>
    .image-container {
        display: inline-block;
        margin: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .image-container:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to load and encode image in base64
def load_image(image_path):
    with open(image_path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

# Display an aesthetic title
st.title("MovieMate 🎥")
#st.header("Personalized Movie Recommendation System")
st.subheader("Personalized Movie Recommendation System")

# Add some famous movie images with hover effects
col1, col2, col3 = st.columns(3)

with col1:
    batman_image = load_image("Images/batman.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{batman_image}" alt="Batman" width="300"></div>',
        unsafe_allow_html=True,
    )

with col2:
    inception_image = load_image("Images/inception.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{inception_image}" alt="Inception" width="300"></div>',
        unsafe_allow_html=True,
    )

with col3:
    avatar_image = load_image("Images/avatar.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{avatar_image}" alt="Avatar" width="300"></div>',
        unsafe_allow_html=True,
    )


# Add the second row of famous movie images with hover effects
col4, col5, col6 = st.columns(3)

with col4:
    titanic_image = load_image("Images/titanic.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{titanic_image}" alt="Titanic" width="300"></div>',
        unsafe_allow_html=True,
    )

with col5:
    matrix_image = load_image("Images/matrix.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{matrix_image}" alt="The Matrix" width="300"></div>',
        unsafe_allow_html=True,
    )

with col6:
    gladiator_image = load_image("Images/gladiator.jpg")  # Replace with the path to your image file
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{gladiator_image}" alt="Gladiator" width="300"></div>',
        unsafe_allow_html=True,
    )


