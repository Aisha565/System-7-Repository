from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, classification_report

# Generate an imbalanced dataset
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    weights=[0.90, 0.10],
    random_state=42
)

# Split dataset while maintaining class distribution
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model without class weighting
model_before = LogisticRegression(max_iter=1000)
model_before.fit(X_train, y_train)

predictions_before = model_before.predict(X_test)

recall_before = recall_score(
    y_test, predictions_before, pos_label=1
)

# Model with balanced class weights
model_after = LogisticRegression(
    max_iter=1000,
    class_weight='balanced'
)

model_after.fit(X_train, y_train)

predictions_after = model_after.predict(X_test)

recall_after = recall_score(
    y_test, predictions_after, pos_label=1
)

# Display results
print("Class Distribution:")
print("Training:", {i: list(y_train).count(i) for i in [0, 1]})
print("Testing:", {i: list(y_test).count(i) for i in [0, 1]})

print("\nRecall Before class_weight:", recall_before)
print("Recall After class_weight:", recall_after)

print("\nClassification Report Before:")
print(classification_report(y_test, predictions_before))

print("\nClassification Report After:")
print(classification_report(y_test, predictions_after))
