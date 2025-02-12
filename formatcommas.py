import pandas as pd

# Read the CSV file
df = pd.read_csv("data-breach.csv")

# Convert 'Records' column to numeric, replacing non-numeric values with 0
df['Records'] = pd.to_numeric(df['Records'], errors='coerce').fillna(0).astype(int)

# Format numbers with commas
df['Records'] = df['Records'].apply(lambda x: f"{x:,}")

# Save to a new CSV file updated file different than original
df.to_csv("databreach_format.csv", index=False)
