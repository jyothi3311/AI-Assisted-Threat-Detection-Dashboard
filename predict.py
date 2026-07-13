import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/random_forest.pkl")

# Load cleaned dataset
df = pd.read_csv("data/cleaned_portscan.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Prepare features
X = df.drop("Label", axis=1)

# Take one sample
sample = X.iloc[[0]]

# Predict
prediction = model.predict(sample)

if prediction[0] == 0:
    print("Prediction: BENIGN")
else:
    print("Prediction: PORTSCAN")