import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

data = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "salary": [30000, 40000, 50000, 60000, 70000],
    "city": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi"]
})

numeric_features = ["age", "salary"]
categorical_features = ["city"]

transformer = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

result = transformer.fit_transform(data)

print("Original Data:\n", data)
print("\nTransformed Data:\n", result)
print("\nOutput Shape:", result.shape)
