import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/battery_data.csv")

# Features & target
X = df[['voltage', 'current', 'time']]
y = df['temperature']

model = RandomForestRegressor(n_estimators=50, max_depth=10)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("✅ Model trained!")
