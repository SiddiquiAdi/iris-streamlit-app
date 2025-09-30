import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="🌸 Iris Flower Prediction",
    page_icon="🌺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for colors and styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
        color: #333333;
    }
    .stButton>button {
        background-color: #ff7eb3;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 25px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff4a91;
        color: white;
    }
    .stNumberInput>div>input {
        border-radius: 10px;
        border: 2px solid #ff7eb3;
        padding: 5px;
        font-size: 16px;
    }
    .stSuccess {
        background-color: #7bed9f !important;
        color: #ffffff !important;
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        border-radius: 15px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: #ff4a91;'>🌸 Iris Flower Prediction 🌸</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #6a0572;'>Enter the features below to predict the Iris flower type</h4>", unsafe_allow_html=True)

# Input fields with a container
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        sl = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
        sw = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
    with col2:
        pl = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
        pw = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[sl, sw, pl, pw]])
    prediction = model.predict(features)
    iris_types = ["Setosa", "Versicolor", "Virginica"]
    flower = iris_types[prediction[0]]

    # Color-coded card for prediction
    color_map = {
        "Setosa": "#ff6b81",
        "Versicolor": "#ffbe76",
        "Virginica": "#7bed9f"
    }

    st.markdown(f"""
        <div style='background-color: {color_map[flower]}; 
                    color: white; 
                    font-size: 24px; 
                    font-weight: bold; 
                    padding: 20px; 
                    border-radius: 20px; 
                    text-align: center;
                    margin-top: 20px;'>
            🌸 Predicted Flower: {flower} 🌸
        </div>
    """, unsafe_allow_html=True)

    # Optional: show flower image
    flower_images = {
        "Setosa": "https://upload.wikimedia.org/wikipedia/commons/5/56/Iris_setosa_2.jpg",
        "Versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        "Virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
    }

    st.image(flower_images[flower], use_column_width=True)
