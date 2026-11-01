# Day 16: Model Tuning and Comparison

## Topics Covered
- Overfitting and underfitting
- Bias-variance trade-off
- Feature scaling and encoding
- ColumnTransformer
- GridSearchCV and RandomizedSearchCV

## Practice Questions
1. Compared Decision Tree training and testing scores for max_depth 1 to 15.
2. Applied StandardScaler and OneHotEncoder using ColumnTransformer.
3. Tuned SVM using GridSearchCV and RandomizedSearchCV.

## Results
- GridSearchCV best score: 97.81%
- RandomizedSearchCV best score: 97.81%
- Both test accuracies: 98.25%
- RandomizedSearchCV was faster in this run.

## Learning Notes
- Overfitting occurs when a model memorizes training data.
- Underfitting occurs when a model fails to learn patterns.
- Bias-variance trade-off balances model complexity.
- Feature scaling brings numerical features to similar ranges.
- One-hot encoding converts categories into numerical values.
- GridSearchCV tests all specified parameter combinations.
- RandomizedSearchCV tests selected parameter combinations.

## Tools
Python, Pandas, Matplotlib and Scikit-learn.
