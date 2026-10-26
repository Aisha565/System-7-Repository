"""Day 10: Simple Linear Regression for house prices."""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

DATA = Path(__file__).resolve().parents[1] / "datasets" / "house_prices.csv"
df = pd.read_csv(DATA)
X = df[["area_sqft"]]
y = df["price_pkr"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)

print("Intercept:", round(model.intercept_, 2))
print("Coefficient (area_sqft):", round(model.coef_[0], 2))
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 2))
print("R2 score:", round(r2_score(y_test, predictions), 4))
print("\nSample predictions:")
print(pd.DataFrame({"Actual price": y_test, "Predicted price": predictions}).head())
area = pd.DataFrame({"area_sqft": [1500]})
print("\nEstimated price for 1500 sqft:", round(model.predict(area)[0], 2), "PKR")
