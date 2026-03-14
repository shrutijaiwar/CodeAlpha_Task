# ===============================
# TASK 2: Exploratory Data Analysis (EDA)
# ===============================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 0: Create dataset if not exists
# -------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

file_path = os.path.join("data", "dataset.csv")

if not os.path.exists(file_path):
    np.random.seed(42)

    data = {
        "Age": np.random.randint(18, 25, 100),
        "Study_Hours": np.random.randint(1, 10, 100),
        "Attendance": np.random.randint(60, 100, 100),
        "Marks": np.random.randint(40, 100, 100),
        "Gender": np.random.choice(["Male", "Female"], 100)
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print("✅ dataset.csv created successfully!")

# -------------------------------
# STEP 1: Load dataset
# -------------------------------
df = pd.read_csv(file_path)

# -------------------------------
# STEP 2: Meaningful Questions
# -------------------------------
"""
1. Does study time affect student marks?
2. Is attendance related to performance?
3. Are there any outliers in marks or attendance?
4. What is the distribution of numerical features?
"""

# -------------------------------
# STEP 3: Data Structure
# -------------------------------
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -------------------------------
# STEP 4: Missing Values
# -------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# STEP 5: Histograms
# -------------------------------
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    plt.figure()
    plt.hist(df[col], bins=20)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig(f"outputs/histogram_{col}.png")
    plt.close()

# -------------------------------
# STEP 6: Boxplots (Outliers)
# -------------------------------
for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.savefig(f"outputs/boxplot_{col}.png")
    plt.close()

# -------------------------------
# STEP 7: Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation.png")
plt.close()

# -------------------------------
# STEP 8: Hypothesis Testing (Visual)
# -------------------------------
plt.figure()
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("outputs/scatter.png")
plt.close()

print("\n🎉 EDA Completed Successfully!")
