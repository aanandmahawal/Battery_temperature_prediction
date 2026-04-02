import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train_model():
    df = pd.read_csv("data/battery_data.csv")

    X = df[['voltage', 'current', 'time']]
    y = df['temperature']

    model = RandomForestRegressor(n_estimators=50, max_depth=10)
    model.fit(X, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")

    return model

# Load or train
if not os.path.exists("model/model.pkl"):
    model = train_model()
else:
    model = joblib.load("model/model.pkl")

st.title("🔋 Battery Temperature Predictor (NASA Dataset)")

voltage = st.number_input("Voltage (V)", value=4.0)
current = st.number_input("Current (A)", value=1.5)
time = st.number_input("Time (s)", value=100.0)

if st.button("Predict"):
    input_data = np.array([[voltage, current, time]])
    pred = model.predict(input_data)

    st.success(f"🌡 Temperature: {pred[0]:.2f} °C")
