# MovieLens 100K – SVD Matrix Factorization (Python 3.10 Compatible)

from surprise import SVD
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import cross_validate, train_test_split

# Load MovieLens 100K dataset
data = Dataset.load_builtin('ml-100k')

# Create SVD model
model = SVD()

# 5-fold Cross Validation (prints RMSE and MAE like sample output)
results = cross_validate(
    model,
    data,
    measures=['RMSE', 'MAE'],
    cv=5,
    verbose=True
)

# Train-test split for final evaluation numbers
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train model
model.fit(trainset)

# Predict ratings for test set
predictions = model.test(testset)

# Calculate RMSE and MAE
rmse = accuracy.rmse(predictions, verbose=False)
mae = accuracy.mae(predictions, verbose=False)

# Final performance printout
print("\nPerformance Evaluation:")
print(f"RMSE: {rmse:.4f}")
print(f"MAE : {mae:.4f}")
