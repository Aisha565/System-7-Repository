import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual = np.array([150000, 180000, 200000, 220000, 250000])
predicted = np.array([155000, 175000, 195000, 225000, 245000])

# Calculate metrics using NumPy
mae = np.mean(np.abs(actual - predicted))
mse = np.mean((actual - predicted) ** 2)
rmse = np.sqrt(mse)
r2 = 1 - np.sum((actual - predicted) ** 2) / np.sum((actual - np.mean(actual)) ** 2)

print("NumPy MAE:", mae)
print("NumPy MSE:", mse)
print("NumPy RMSE:", rmse)
print("NumPy R2:", r2)

# Verify using Scikit-learn
print("\\nScikit-learn MAE:", mean_absolute_error(actual, predicted))
print("Scikit-learn MSE:", mean_squared_error(actual, predicted))
print("Scikit-learn RMSE:", np.sqrt(mean_squared_error(actual, predicted)))
print("Scikit-learn R2:", r2_score(actual, predicted))
