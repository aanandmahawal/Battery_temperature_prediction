import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv("data/nasa_power_global_daily.csv")

# Features & target
features = ['T2M_MAX', 'T2M_MIN', 'RH2M', 'WS10M', 'PRECTOTCORR']
target = 'T2M'

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=50, max_depth=10)
model.fit(X_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("✅ Model trained and saved!")