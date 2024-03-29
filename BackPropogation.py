import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Initializing weights with values sampled from a uniform distribution
def initialize_weights(shape):
    return np.random.uniform(-0.1, 0.1, shape)

# Input data (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Target outputs
Y = np.array([[0], [1], [1], [0]])

# Defining the number of units in each layer
input_units = 2
hidden_units = 2
output_units = 1

# Seed for reproducibility
np.random.seed(1)

# Initializing weights and biases
v = initialize_weights((hidden_units, input_units))
w = initialize_weights((output_units, hidden_units))
b1 = np.zeros((hidden_units, 1))
b2 = np.zeros((output_units, 1))

# Hyperparameters
learning_rate = 0.1
epochs = 10000

# Lists to store epoch, squared error, and accuracy
epoch_list = []
accuracy_list = []
squared_error_list = []

# Training loop
for epoch in range(epochs):
    squared_error_sum = 0
    # Iterating through each input-output pair
    for x, y_true in zip(X, Y):
        x = x.reshape((1, 2))
        y_true = y_true.reshape((1, 1))

        # Forward pass
        z = sigmoid(np.dot(v, x.T) + b1)
        y_pred = np.dot(w, z) + b2

        # Calculating squared error
        squared_error = np.mean(np.square(y_true - y_pred))
        squared_error_sum += squared_error

        # Backpropagation
        delta_w = learning_rate * np.dot((y_true - y_pred) * sigmoid_derivative(y_pred), z.T)
        delta_v = learning_rate * np.dot(np.dot(w.T, (y_true - y_pred) * sigmoid_derivative(y_pred)) * sigmoid_derivative(z), x)

        # Updating weights and biases
        w += delta_w
        v += delta_v
        b2 += learning_rate * (y_true - y_pred)
        b1 += learning_rate * np.dot(w.T, (y_true - y_pred) * sigmoid_derivative(y_pred))

    # Calculating accuracy and store values
    if epoch % 1000 == 0:
        epoch_list.append(epoch)
        accuracy = 1 - squared_error_sum / len(X)
        accuracy_list.append(accuracy)
        squared_error_list.append(squared_error_sum / len(X))

# Printing final weights and biases
print("Final v weights:")
print(v)
print("Final w weights:")
print(w)

# Printing outputs for each input
print("Outputs for data:")
for x, y_true in zip(X, Y):
    x = x.reshape((1, 2))
    z = sigmoid(np.dot(v, x.T) + b1)
    y_pred = np.dot(w, z) + b2
    print(f"Input: {x.flatten()}, Predicted Output: {y_pred.flatten()}, Actual Output: {y_true}")

# Printing epoch, squared error, and accuracy
print("Epoch\tSquared Error\tAccuracy")
for i in range(len(epoch_list)):
    print(f"{epoch_list[i]}\t{squared_error_list[i]}\t{accuracy_list[i]}")

