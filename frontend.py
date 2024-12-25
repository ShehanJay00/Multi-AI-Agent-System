import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="MovieMate - Your Movie Companion", layout="centered")

# Display an aesthetic title
st.title("\ud83c\udfa5 Welcome to MovieMate \ud83c\udfa5")
st.subheader("Your Personalized Movie Recommendation System")

# Add some famous movie images
col1, col2, col3 = st.columns(3)
with col1:
    batman_image = Image.open("batman.jpg")  # Replace with the path to your image file
    st.image(batman_image, caption="Batman", use_column_width=True)

with col2:
    inception_image = Image.open("inception.jpg")  # Replace with the path to your image file
    st.image(inception_image, caption="Inception", use_column_width=True)

with col3:
    avatar_image = Image.open("avatar.jpg")  # Replace with the path to your image file
    st.image(avatar_image, caption="Avatar", use_column_width=True)

# Add a modern text box for asking questions
st.write("\n")
question = st.text_input("Ask MovieMate a question about movies, actors, directors, or recommendations:", placeholder="E.g., Recommend me a movie like Inception")

# Respond to the question
if question:
    # Placeholder response - Replace with your movie recommendation logic
    response = "Great choice! Based on your interest, you might enjoy 'Interstellar.'"
    st.markdown(f"**MovieMate says:** {response}")
