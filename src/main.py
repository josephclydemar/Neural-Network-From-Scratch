import numpy as np

inputs = np.random.uniform(low=-4, high=4, size=(3,))
weights = np.random.uniform(low=-2, high=2, size=(5,3))
biases = np.random.uniform(low=-1, high=1, size=(5,))

output = np.dot(weights, inputs) + biases
print('Input Vector:\n', inputs, '\n')
print('Weights:\n', weights, '\n')
print('Biases:\n', biases, '\n')
print('Output:\n', output, '\n')