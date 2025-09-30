import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🌸 Iris Flower Prediction App")

# Input fields
sl = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sw = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
pl = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
pw = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[sl, sw, pl, pw]])
    prediction = model.predict(features)
    iris_types = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"Predicted Flower: {iris_types[prediction[0]]}")
