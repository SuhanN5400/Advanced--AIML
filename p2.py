import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- Step 1: Generate a simple binary dataset ---
X, y = make_classification(
    n_samples=100,       # number of data points
    n_features=2,        # 2 features for easy visualization
    n_informative=2,     # both features are useful
    n_redundant=0,       # no duplicate features
    n_clusters_per_class=1,
    flip_y=0,            # no noise
    random_state=42
)

# --- Step 2: Split into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- Step 3: Create and train Perceptron model ---
model = Perceptron(max_iter=1000, eta0=1, random_state=42)
model.fit(X_train, y_train)

# --- Step 4: Evaluate accuracy ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# --- Step 5: Plot the decision boundary ---
xx, yy = np.meshgrid(
    np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100),
    np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100)
)

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap='coolwarm')
plt.title("Perceptron Classification")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
