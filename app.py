import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Function to train model
def train_model():
    df = pd.read_csv("data/battery_data.csv")

    X = df[['voltage', 'current', 'time']]
    y = df['temperature']

    model = RandomForestRegressor(n_estimators=50, max_depth=10)
    model.fit(X, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")

    return model

# Load or train model
if not os.path.exists("model/model.pkl"):
    model = train_model()
else:
    model = joblib.load("model/model.pkl")

# ---------------- UI ---------------- #

st.set_page_config(page_title="Battery Temp Predictor", layout="centered")

st.title("🔋 Battery Temperature Prediction System")

# 🔥 Dataset Info (IMPORTANT ADDITION)
st.markdown("""
### 📊 Dataset Used
- NASA Lithium-Ion Battery Dataset  
- Battery ID: **B0005**  
- Source: NASA Ames Prognostics Center  

This model predicts battery temperature using:
- Voltage ⚡  
- Current 🔌  
- Time ⏱️  
""")

st.divider()

st.subheader("Enter Battery Parameters")

# Inputs
voltage = st.number_input("Voltage (V)", value=4.0)
current = st.number_input("Current (A)", value=1.5)
time = st.number_input("Time (s)", value=100.0)

# Prediction
if st.button("Predict Temperature"):
    input_data = np.array([[voltage, current, time]])
    pred = model.predict(input_data)

    st.success(f"🌡 Predicted Battery Temperature: {pred[0]:.2f} °C")

# Footer
st.markdown("---")
st.caption("⚙️ Built using NASA B0005 Battery Dataset")
