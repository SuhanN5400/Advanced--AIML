import tensorflow as tf, numpy as np, matplotlib.pyplot as plt
from tensorflow.keras import layers, models

# Load and normalize
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
names = ['airplane','auto','bird','cat','deer','dog','frog','horse','ship','truck']

# Model
m = models.Sequential([
    layers.Conv2D(32, 3, activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D(), layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(), layers.Conv2D(64, 3, activation='relu'),
    layers.Flatten(), layers.Dense(64, activation='relu'), layers.Dense(10)
])
m.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['acc'])
m.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test), verbose=2)

# Predict and show
pred = tf.argmax(tf.nn.softmax(m(x_test[:16])), axis=1).numpy()
plt.figure(figsize=(9,9))
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.imshow(x_test[i])
    plt.title(f"P:{names[pred[i]]}\nT:{names[y_test[i][0]]}", color='green' if pred[i]==y_test[i] else 'red', fontsize=8)
    plt.axis('off')
plt.tight_layout(); plt.show()
