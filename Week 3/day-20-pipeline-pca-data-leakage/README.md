# Day 20 - Pipeline, PCA and Data Leakage

## Objective
Understand Scikit-learn Pipelines, PCA and Data Leakage.

## Tasks Completed
1. Created a Pipeline using StandardScaler, PCA and Logistic Regression.
2. Applied correct preprocessing after train-test split.
3. Demonstrated incorrect preprocessing using the complete dataset.
4. Compared both approaches.

## Dataset
Breast Cancer Dataset from Scikit-learn.

- Original samples: 569
- Original features: 30
- PCA components: 10
- Explained variance target: 95%

## Results

| Approach | Accuracy |
|---|---:|
| Correct Pipeline | 97.37% |
| Data Leakage | 96.49% |

## Key Learning
- Pipelines combine preprocessing and machine learning steps.
- PCA reduces dimensionality.
- Data leakage occurs when test data information influences training.
- Preprocessing should be fitted only on training data.

## Tools
Python, NumPy, Scikit-learn.

## Status
Completed Successfully.
