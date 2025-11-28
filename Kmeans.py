import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Generate simple sample data
np.random.seed(42)
data1 = np.random.randn(100, 2) + np.array([2, 2])
data2 = np.random.randn(100, 2) + np.array([-2, -2])
data3 = np.random.randn(100, 2) + np.array([2, -2])
X = np.vstack([data1, data2, data3])

# Step 2: Plot BEFORE clustering
plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.scatter(X[:,0], X[:,1], color='blue',cmap='coolwarm')
plt.title("Before K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)

# Step 3: Apply K-Means
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

# Step 4: Plot AFTER clustering
plt.subplot(1, 2, 2)
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=200, marker='X', label='Centroids')
plt.title("After K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Step 5: Evaluate clustering quality
inertia = kmeans.inertia_
sil_score = silhouette_score(X, labels)

print(f"Inertia (Lower is better): {inertia:.2f}")
print(f"Silhouette Score (Closer to 1 is better): {sil_score:.4f}")
