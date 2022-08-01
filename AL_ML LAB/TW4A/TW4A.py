# SHATA BHI KYA NAI SAMJHRA! SKIP MARO BC ISSE
import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print('Input:')
print(x)

y = np.array([[0], [1], [1], [0]])
print('Actual output: ')
print(y)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivatives_sigmoid(x):
    return x * (1 - x)


# initializing variables
epoch = 6000
lr = 0.15
inputlayer_neurons = x.shape[1]
hiddenlayer_neurons = 2
output_neurons = 1

# initializing weight and bias
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# training the model
for i in range(epoch):
    # forward propagation
    hidden_layer_input1 = np.dot(x, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1 = np.dot(hiddenlayer_activations, wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)

    # backpropagation
    e = y - output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    d_output = e * slope_output_layer
    error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += x.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print('Output from the model: ')
print(output)
print(np.round(output))
