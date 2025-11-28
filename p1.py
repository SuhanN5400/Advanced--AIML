import numpy as np
import matplotlib.pyplot as plt

# --- Activation Functions ---
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    e_x = np.exp(x - np.max(x))   # to avoid overflow
    return e_x / e_x.sum(axis=0)

# --- Input values ---
x = np.linspace(-10, 10, 200)

# --- Compute function outputs ---
y_sigmoid = sigmoid(x)
y_tanh = tanh(x)
y_relu = relu(x)
y_softmax = softmax(np.array([x, 0.5*x, 0.2*x]))

# --- Plotting ---
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_sigmoid, 'b')
plt.title("Sigmoid Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y_tanh, 'r')
plt.title("Tanh Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, y_relu, 'g')
plt.title("ReLU Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, y_softmax[0], label='Set 1')
plt.plot(x, y_softmax[1], label='Set 2')
plt.plot(x, y_softmax[2], label='Set 3')
plt.title("Softmax Function")
plt.xlabel("Input")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
