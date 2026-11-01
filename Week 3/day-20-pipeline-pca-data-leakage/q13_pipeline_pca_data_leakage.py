
# Q13: Pipeline, PCA and Data Leakage

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

print("Original Dataset Shape:", X.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Approach 1: Correct preprocessing using Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=0.95)),
    ("classifier", LogisticRegression(max_iter=5000))
])

pipeline.fit(X_train, y_train)
correct_predictions = pipeline.predict(X_test)

correct_accuracy = accuracy_score(
    y_test, correct_predictions
)

print("\n--- Correct Approach (Pipeline) ---")
print("Accuracy:", correct_accuracy)
print("PCA Components:", pipeline.named_steps["pca"].n_components_)

# Approach 2: Incorrect preprocessing (Data Leakage)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

X_train_leak, X_test_leak, y_train_leak, y_test_leak = train_test_split(
    X_pca, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train_leak, y_train_leak)

leak_predictions = model.predict(X_test_leak)

leak_accuracy = accuracy_score(
    y_test_leak, leak_predictions
)

print("\n--- Incorrect Approach (Data Leakage) ---")
print("Accuracy:", leak_accuracy)

# Compare both approaches
print("\n--- Accuracy Comparison ---")
print("Correct Pipeline:", correct_accuracy)
print("Data Leakage:", leak_accuracy)

print("\nQ13 Completed Successfully!")
