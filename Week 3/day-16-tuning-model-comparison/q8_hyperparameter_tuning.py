import time
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC())
])

parameters = {
    "svm__C": [0.1, 1, 10],
    "svm__kernel": ["linear", "rbf"],
    "svm__gamma": ["scale", "auto"]
}

grid = GridSearchCV(pipeline, parameters, cv=3, scoring="accuracy")
start = time.time()
grid.fit(X_train, y_train)
grid_time = time.time() - start

random_search = RandomizedSearchCV(
    pipeline, parameters, n_iter=5, cv=3,
    scoring="accuracy", random_state=42
)
start = time.time()
random_search.fit(X_train, y_train)
random_time = time.time() - start

print("GridSearch Best Parameters:", grid.best_params_)
print("GridSearch Best Score:", grid.best_score_)
print("GridSearch Time:", round(grid_time, 3), "seconds")

print("\nRandomizedSearch Best Parameters:", random_search.best_params_)
print("RandomizedSearch Best Score:", random_search.best_score_)
print("RandomizedSearch Time:", round(random_time, 3), "seconds")

print("\nGridSearch Test Accuracy:", grid.score(X_test, y_test))
print("RandomizedSearch Test Accuracy:", random_search.score(X_test, y_test))
