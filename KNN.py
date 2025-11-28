from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Step 1: Load the Iris dataset
iris = load_iris()

# Step 2: Create feature and target data
X = iris.data
y = iris.target

# Step 3: Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the KNN classifier
k = 5  # number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = knn.predict(X_test)

# Step 6: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")

# Step 7: Display correct and wrong predictions
results = pd.DataFrame({
    'Actual': [iris.target_names[i] for i in y_test],
    'Predicted': [iris.target_names[i] for i in y_pred]
})

# Step 8: Separate correct and wrong predictions
correct = results[results['Actual'] == results['Predicted']]
wrong = results[results['Actual'] != results['Predicted']]

print("✅ Correct Predictions:")
print(correct.to_string(index=False))

print("\n❌ Wrong Predictions:")
print(wrong.to_string(index=False) if not wrong.empty else "None — all predictions correct!")
