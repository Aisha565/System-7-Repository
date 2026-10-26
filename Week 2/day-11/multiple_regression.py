"""Day 11: Multiple Linear Regression using several house features."""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

DATA = Path(__file__).resolve().parents[1] / "datasets" / "house_prices.csv"
df = pd.read_csv(DATA)
features = ["area_sqft", "bedrooms", "age_years"]
X, y = df[features], df["price_pkr"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)

print("Intercept:", round(model.intercept_, 2))
print("\nCoefficients:")
for feature, coefficient in zip(features, model.coef_):
    print(f"{feature}: {coefficient:.2f}")
print("\nMAE:", round(mean_absolute_error(y_test, predictions), 2))
print("R2 score:", round(r2_score(y_test, predictions), 4))
sample = pd.DataFrame([{"area_sqft": 1500, "bedrooms": 3, "age_years": 5}])
print("\nEstimated price for sample house:", round(model.predict(sample)[0], 2), "PKR")
