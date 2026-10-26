"""Day 08: Explore a dataset with Pandas and NumPy."""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "datasets" / "student_performance.csv"
df = pd.read_csv(DATA)

print("First 5 rows:\n", df.head(), "\n")
print("Shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDescriptive statistics:\n", df.describe())
numeric = df.select_dtypes(include=np.number)
print("\nNumPy means:\n", np.mean(numeric, axis=0))
