import pandas as pd
import numpy as np
from sklearn.utils import shuffle

np.random.seed(42)

# Total samples
n_samples = 50000
half = n_samples // 2

# Helper function to generate feature arrays
def generate_data(n, overfill):
    return pd.DataFrame({
        "Tank_Level": np.random.uniform(80, 100, n) if overfill else np.random.uniform(10, 75, n),
        "Flow_Rate": np.random.uniform(100, 500, n) if overfill else np.random.uniform(-500, 100, n),
        "Feed_Consumption": np.random.uniform(10, 300, n),
        "Product_Generation": np.random.uniform(50, 200, n),
        "Byproduct": np.random.uniform(0, 50, n),
        "Peak_Hour": np.random.randint(0, 2, n),
        "Pressure": np.random.uniform(5, 10, n) if overfill else np.random.uniform(0.5, 7, n),
        "Temperature": np.random.uniform(20, 80, n),
        "Nitrogen": np.random.uniform(0, 100, n),
        "Oxygen": np.random.uniform(0, 21, n),
        "CO2": np.random.uniform(0, 10, n),
        "Methane": np.random.uniform(0, 100, n),
        "Overfill": np.full(n, overfill, dtype=int)
    })

# Generate balanced dataset
df_overfill = generate_data(half, 1)
df_normal = generate_data(half, 0)

# Combine and shuffle
df = pd.concat([df_overfill, df_normal], ignore_index=True)
df = shuffle(df, random_state=42).reset_index(drop=True)

# ✅ Save to CSV
df.to_csv("synthetic_tank_data.csv", index=False)
print("💾 Dataset saved as 'synthetic_tank_data.csv'")

# Preview
print(df.head())
print("\n✅ Dataset shape:", df.shape)
print("⚖️ Class balance:\n", df['Overfill'].value_counts())
