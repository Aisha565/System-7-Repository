import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load Iris dataset
data = load_iris()
X = data.data

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce data to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_pca)

# Calculate explained variance
explained_variance = pca.explained_variance_ratio_

print("Original Dataset Shape:", X.shape)
print("Reduced Dataset Shape:", X_pca.shape)

print("\nExplained Variance Ratio:", explained_variance)
print("Total Explained Variance:", explained_variance.sum())

# Plot PCA clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters,
    cmap='viridis',
    edgecolors='black'
)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA - K-Means Clustering')
plt.colorbar(label='Cluster')
plt.grid(True)

plt.savefig('pca_clusters.png')
plt.show()

print("\nPCA cluster plot saved successfully!")
