import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_portscan.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Function to assign risk level
def calculate_risk(label):
    if label == "PortScan":
        return "High"
    else:
        return "Low"

# Add Risk Level column
df["Risk Level"] = df["Label"].apply(calculate_risk)

# Display first few rows
print(df[["Label", "Risk Level"]].head())

# Save dataset
df.to_csv("data/risk_data.csv", index=False)

print("\nRisk score generated successfully!")