"""Day 09: Split a dataset into training and testing sets."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

DATA = Path(__file__).resolve().parents[1] / "datasets" / "student_performance.csv"
df = pd.read_csv(DATA)
X = df[["study_hours", "attendance"]]
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Total rows:", len(df))
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("\nTraining features:\n", X_train.head())
print("\nTesting target values:\n", y_test.head())
