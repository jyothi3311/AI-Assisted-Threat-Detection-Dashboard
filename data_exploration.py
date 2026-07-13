import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")

# Basic Information
print("========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== LABEL DISTRIBUTION ==========")
print(df[" Label"].value_counts())