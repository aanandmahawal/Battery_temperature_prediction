import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model/model.pkl")

st.set_page_config(page_title="Battery Temp Predictor")

st.title("🔋 Battery Temperature Prediction (NASA Data)")

st.write("Enter environmental conditions:")

# Inputs
t2m_max = st.number_input("Max Temperature (°C)", value=30.0)
t2m_min = st.number_input("Min Temperature (°C)", value=20.0)
rh = st.number_input("Humidity (%)", value=70.0)
ws = st.number_input("Wind Speed (m/s)", value=3.0)
rain = st.number_input("Precipitation", value=1.0)

# Prediction
if st.button("Predict Temperature"):
    input_data = np.array([[t2m_max, t2m_min, rh, ws, rain]])
    prediction = model.predict(input_data)

    st.success(f"🌡 Predicted Battery Temp: {prediction[0]:.2f} °C")