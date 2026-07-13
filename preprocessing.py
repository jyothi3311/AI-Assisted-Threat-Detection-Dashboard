import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()
print("After Removing Duplicates:", df.shape)

# Remove missing values
df = df.dropna()
print("After Removing Missing Values:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_portscan.csv", index=False)

print("\nCleaned dataset saved successfully!")