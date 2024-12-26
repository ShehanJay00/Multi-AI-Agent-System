import streamlit as st
from PIL import Image
import base64

def load_image(image_path):
    with open(image_path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

def frontend():
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

    # Inject custom CSS for fonts and center alignment
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Open+Sans:wght@400&display=swap');
        
        .title {
            text-align: center;
            font-family: 'Roboto', sans-serif;
            font-size: 3.5em;
            color: #C0C0C0;
        }

        .subtitle {
            text-align: center;
            font-family: 'Open Sans', sans-serif;
            font-size: 1.5em;
            color: #808080;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Centered title and subtitle with custom fonts
    st.markdown('<div class="title">MovieMate🎥</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Personalized Movie Recommendation System</div>', unsafe_allow_html=True)

    # Add spacing between title and chat interface
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Add description for MovieMate
    st.markdown(
        """
        <style>
        .description {
            color: #C0C0C0; 
            font-size: 16px;
            line-height: 1.6;
            font-family: Arial, sans-serif;
            text-align: justify;
        }
        </style>
        <div class="description">
            <b>Welcome to MovieMate 🎥 – Your Ultimate Movie Companion!</b>  
            MovieMate is a cutting-edge platform designed to enhance your movie-watching experience, powered by an advanced Multi-Agent System. Whether you're a casual viewer or a cinephile, MovieMate is here to help you discover, explore, and enjoy movies like never before. With personalized recommendations, curated lists, and advanced search capabilities, MovieMate brings the world of cinema to your fingertips. Leveraging the power of intelligent agents, MovieMate provides tailored movie suggestions, interactive queries for instant answers about films, actors, and genres, and a visually engaging interface that ensures an unparalleled user experience. Whether you're looking for your next favorite film or diving deep into cinematic trivia, MovieMate is your ultimate destination for all things movies. Start your journey into the world of cinema with MovieMate today!
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)

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
        tofe_image = load_image("Images/TofE.jpg")  # Replace with the path to your image file
        st.markdown(
            f'<div class="image-container"><img src="data:image/jpeg;base64,{tofe_image}" alt="Avatar" width="300"></div>',
            unsafe_allow_html=True,
        )

    # Add spacing between rows
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Add the second row of famous movie images with hover effects
    col4, col5, col6 = st.columns(3)

    with col4:
        moana_image = load_image("Images/Moana.jpg")  # Replace with the path to your image file
        st.markdown(
            f'<div class="image-container"><img src="data:image/jpeg;base64,{moana_image}" alt="Titanic" width="300"></div>',
            unsafe_allow_html=True,
        )

    with col5:
        matrix_image = load_image("Images/Matrix.jpg")  # Replace with the path to your image file
        st.markdown(
            f'<div class="image-container"><img src="data:image/jpeg;base64,{matrix_image}" alt="The Matrix" width="300"></div>',
            unsafe_allow_html=True,
        )

    with col6:
        gladiator_image = load_image("Images/Galadiator.jpg")  # Replace with the path to your image file
        st.markdown(
            f'<div class="image-container"><img src="data:image/jpeg;base64,{gladiator_image}" alt="Gladiator" width="300"></div>',
            unsafe_allow_html=True,
        )

    # Add spacing between rows
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.write("<div style='height: 30px;'></div>", unsafe_allow_html=True)



        # Inject custom CSS for styling
    st.markdown(
        """
        <style>
        /* Style the text area */
        .stTextArea textarea {
            font-family: 'Open Sans', sans-serif;
            font-size: 16px;
            color: #000000;
            border: 2px solid #808080;
            border-radius: 8px;
            padding: 10px;
            background-color: #FFFFFF;
        }

        /* Style the button */
        .stButton button {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            background-color: #FF0000;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 8px 16px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .stButton button:hover {
            background-color: 	#000000;
            transform: scale(1.05);
            cursor: pointer;
        }

        /* Style the spinner */
        .css-1gx4ub2 {
            font-family: 'Open Sans', sans-serif;
            font-size: 16px;
            color: #2E86C1;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
