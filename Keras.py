import tensorflow as tf, numpy as np, matplotlib.pyplot as plt

# Load CIFAR-10 dataset and normalize pixel values to [0, 1]
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Class labels for CIFAR-10
names = ['airplane','auto','bird','cat','deer','dog','frog','horse','ship','truck']

# Define CNN model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(32,32,3)),  # Conv layer
    tf.keras.layers.MaxPooling2D(),                                           # Pooling
    tf.keras.layers.Conv2D(64, 3, activation='relu'),                         # Conv layer
    tf.keras.layers.MaxPooling2D(),                                           # Pooling
    tf.keras.layers.Conv2D(64, 3, activation='relu'),                         # Conv layer
    tf.keras.layers.Flatten(),                                               # Flatten features
    tf.keras.layers.Dense(64, activation='relu'),                            # Dense hidden layer
    tf.keras.layers.Dense(10)                                                # Output layer for 10 classes
])

# Compile model with optimizer, loss function, and accuracy metric
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model for 10 epochs with validation on test set
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test), verbose=2)

# Predict first 16 test images using softmax and argmax
pred = tf.argmax(tf.nn.softmax(model(x_test[:16])), axis=1).numpy()

# Plot the predictions with actual labels
plt.figure(figsize=(9,9))
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.imshow(x_test[i])
    plt.title(f"P:{names[pred[i]]}\nT:{names[y_test[i][0]]}",
              color='green' if pred[i]==y_test[i] else 'red', fontsize=8)
    plt.axis('off')
plt.tight_layout(); plt.show()
