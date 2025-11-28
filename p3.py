import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# --- Step 1: Load and preprocess the dataset ---
X, y = load_iris(return_X_y=True)

# Standardize the input features (mean=0, std=1)
X = StandardScaler().fit_transform(X)

# One-hot encode the target labels (3 classes → 3 neurons in output)
y = tf.keras.utils.to_categorical(y)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- Step 2: Build the Deep Neural Network ---
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')   # Output layer for 3 classes
])

# --- Step 3: Compile the model ---
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# --- Step 4: Train the model ---
model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=8,
    validation_split=0.2,
    verbose=1
)

# --- Step 5: Evaluate the model ---
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy * 100:.2f}%")
print(f"Test Loss: {loss:.4f}")
