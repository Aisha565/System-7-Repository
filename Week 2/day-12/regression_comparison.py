"""Day 12: Compare simple and multiple linear regression."""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

DATA = Path(__file__).resolve().parents[1] / "datasets" / "house_prices.csv"
df = pd.read_csv(DATA)
y = df["price_pkr"]
X_simple = df[["area_sqft"]]
X_multiple = df[["area_sqft", "bedrooms", "age_years"]]
X1_train, X1_test, y_train, y_test = train_test_split(
    X_simple, y, test_size=0.2, random_state=42
)
X2_train, X2_test, _, _ = train_test_split(
    X_multiple, y, test_size=0.2, random_state=42
)
models = [
    ("Simple Linear Regression", LinearRegression().fit(X1_train, y_train), X1_test),
    ("Multiple Linear Regression", LinearRegression().fit(X2_train, y_train), X2_test),
]
for name, model, X_test in models:
    pred = model.predict(X_test)
    print(f"\n{name}")
    print("MAE:", round(mean_absolute_error(y_test, pred), 2))
    print("R2 score:", round(r2_score(y_test, pred), 4))
