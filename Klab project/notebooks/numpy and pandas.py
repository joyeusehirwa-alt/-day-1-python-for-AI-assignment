import numpy as np
import pandas as pd

# NumPy Operations[cite: 1]
# 1. 1-D array statistics[cite: 1]
arr_1d = np.array([14.2, 28.5, 33.1, 42.0, 58.9, 61.3])
print(f"Mean: {arr_1d.mean():.2f}, Std: {arr_1d.std():.2f}, Min: {arr_1d.min()}, Max: {arr_1d.max()}")[cite: 1]

# 2. 2-D array shapes[cite: 1]
arr_2d = np.array([[10, 12, 15, 18], [20, 25, 22, 29], [30, 31, 35, 38]])
print("Original shape:", arr_2d.shape)[cite: 1]
print("Transpose shape:", arr_2d.T.shape)[cite: 1]

# 3. Broadcasting subtraction[cite: 1]
col_means = arr_2d.mean(axis=0)
centered_2d = arr_2d - col_means
print("Centered 2D Array:\n", centered_2d)[cite: 1]

# Pandas Operations[cite: 1]
# 1. Create DataFrame with 4 columns, 6 rows, text column, missing value[cite: 1]
data = {
    "model_id": ["M1", "M2", "M3", "M4", "M5", "M6"],[cite: 1]
    "architecture": ["CNN", "ResNet", "Transformer", "LSTM", "Transformer", "CNN"],[cite: 1]
    "accuracy": [0.78, 0.85, 0.93, np.nan, 0.91, 0.82],  # Missing value included[cite: 1]
    "latency_ms": [12, 24, 65, 40, 58, 15]
}
df = pd.DataFrame(data)

# 2. DataFrame inspection[cite: 1]
print("\n--- INFO ---")
df.info()[cite: 1]
print("\n--- DESCRIBE ---")
print(df.describe())[cite: 1]
print("\n--- MISSING VALUES ---")
print(df.isna().sum())[cite: 1]

# 3. Filter and sort[cite: 1]
filtered_df = df[df["latency_ms"] < 50].sort_values(by="accuracy", ascending=False)
print("\nFiltered & Sorted:\n", filtered_df)[cite: 1]

# 4. Derived boolean column[cite: 1]
df["passed_test"] = (df["accuracy"] >= 0.80) & (df["latency_ms"] < 50)
print("\nWith Derived Column:\n", df)[cite: 1]