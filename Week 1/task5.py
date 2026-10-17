
import numpy as np

# Create a 3x3 matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Display the original matrix
print("--- Original Matrix ---")
print(matrix)

# Display shape and dimensions
print("\nShape:", matrix.shape)
print("Dimensions:", matrix.ndim)

# Access an element and a row
print("\nElement at row 1, column 2:", matrix[0, 1])
print("First row:", matrix[0])

# Perform mathematical operations
print("\nMatrix + 5:")
print(matrix + 5)

print("\nMatrix * 2:")
print(matrix * 2)

# Calculate statistics
print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Minimum:", np.min(matrix))
print("Maximum:", np.max(matrix))

print("\nNumPy operations completed successfully!")
