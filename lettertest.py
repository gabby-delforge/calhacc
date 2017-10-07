import converter
import numpy as np

training_data = converter.convert("MNISTfiles/train_images", "MNISTfiles/train_labels")
test_data = converter.convert("MNISTfiles/test_images", "MNISTfiles/test_labels")

num_epochs = 1000
mini_batch = 264
learn_rate = 10

class Network(object):
	""" Sizes is an array whose length equals the number of layers in the NN, 
	and whose values represent the number of nodes in each layer. 
	Biases and weights are initialized randomly to start with. 
	biases format - list of length layers- 1 with inner lists of length size[i], the size of the layer indexed with i
	weights format - list of length layers with inner lists of length size[i], the size of the layer indexed with i

	"""
	def __init__(self, sizes):
		self.layers = len(sizes)
		self.sizes = sizes
		self.bias = [np.random.randn(size[i], layers - 1) for i in layers - 1]
		self.weights = [np.random.randn(size[i], layers) for i in layers]

	""" Given an input a, feeds the input through each layer to get an output.
	a - list of 784 opacity values (0-255)
	"""
	def get_output(self, a):
		for i in range(layers - 1):

	"""Uses stochastic gradient descent to minimize loss. 
		rate - learning rate
		epochs - number of times to run through training
		mini_batch_size - size of mini_batch to use to update weights - can be resource-heavy
		test_data - used for tracking progress, resource-heavy. """
	def learn(self, rate, epochs, mini_batch_size, test_data = None):

	"""Uses the training data in MINI_BATCH to update the network's weights and biases. """
	def update_mini_batch(self, mini_batch, rate):

	def loss(self, )


def sigmoid(z):
	return 1.0/(1.0 + np.exp(-z))

"""Derivative of the sigmoid function. """
def sigmoid_prime(z):


net = Network([784, 49 ,10])








