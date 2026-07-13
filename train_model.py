import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load cleaned dataset
df = pd.read_csv("data/cleaned_portscan.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert labels into numbers
df["Label"] = df["Label"].map({
    "BENIGN": 0,
    "PortScan": 1
})

# Replace Infinity values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove rows containing NaN
df.dropna(inplace=True)

# Features and Target
X = df.drop("Label", axis=1)
y = df["Label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/random_forest.pkl")

print("\nModel saved successfully!")