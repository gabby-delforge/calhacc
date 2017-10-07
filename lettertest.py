import converter
import numpy as np

# Inspired by and referenced from Michael Nielsen's discussion of handwriting recognition using neural networks.

training_data = converter.convert("MNISTfiles/train_images", "MNISTfiles/train_labels")
test_data = converter.convert("MNISTfiles/test_images", "MNISTfiles/test_labels")

num_epochs = 1000
mini_batch_size = 264
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
		for w, b in zip(self.weights, self.biases):
			a = sigmoid(np.dot(w, a) + b)
		return a

	"""Uses stochastic gradient descent to minimize loss. 
		rate - learning rate
		epochs - number of times to run through training
		mini_batch_size - size of mini_batch to use to update weights - can be resource-heavy
		test_data - used for tracking progress, resource-heavy. """
	def learn(self, rate, mini_batch_size, test_data = None):
		if test_data:
			num_tests = len(training_data)
		n = len(training_data)
		for j in xrange(epochs):
			random.shuffle(training_data)
			mini_batches = [training_data[k + mini_batch_size] for k in xrange(0, n, mini_batch_size)]
			for batch in mini_batches:
				self.update_mini_batch(mini_batch) #Updates weights and biases
			if test_data:
				print("Epoch " + j + ": " + self.evaluate(test_data) + "/" + num_tests)
			else:
				print("Epoch " + j + " complete")


	"""Uses the training data in MINI_BATCH to update the network's weights and biases. """
	def update_mini_batch(self, mini_batch):
		gradient_w = np.zeros(x.shape) for x in self.weights
		gradient_b = np.zeros(y.shape) for y in self.bias
		for x, y in mini_batch:
			d_grad_w, d_grad_b = self.loss(x, y)
			gradient_w = [gw + dgw for gw, dgw in zip(gradient_w, d_grad_w)]
			gradient_b = [gb + dgb for gb, dgb in zip(gradient_b, d_grad_b)]
		self.weights = [w - (learning_rate/len(mini_batch))* gradient_w for w, gradient_w in zip(self.weights, gradient_w)]
		self.bias = [b - (learning_rate/len(mini_batch))* gradient_b for b, gradient_b in zip(self.bias, gradient_b)]

	def evaluate(self, test_data):
		result = [(argmax(get_output(x)), y) for (x, y) in test_data]
		return sum([(x==y) for (x, y) in result])

	def loss(self, x, y):
		b = [np.zeros(x.shape) for x in self.bias]
		w = [np.zeros(y.shape) for y in self.weights]
		activation = x
		activationlist = [x]
		zlist = []
		for bias, weight in zip(self.biases, self.weights):
			z = np.dot(weight, activation) + bias
			zlist.append(z)
			activation = sigmoid(z)
			activationlist.append(activation)

		error = (activationlist[len(activationlist) - 1] - y) * sigomid_prime(zlist[len(zlist) - 1])
		b[len(b) - 1] = error
		w[len(w) - 1] = np.dot(error, activationlist[len(activationlist) - 2].transpose())


		for l in self.layers[1:]:
			z = zlist[len(zlist) - 1]
			error = np.dot(self.weights[len(self.weights) - l], error) * sigmoid_prime(z)
			b[len(b) - 1] = error
			w[len(w) - 1] = np.dot(error, activationlist[len(activationlist) - l].transpose())
		return (b, w)

			


def sigmoid(z):
	return 1.0/(1.0 + np.exp(-z))

"""Derivative of the sigmoid function. """
def sigmoid_prime(z):
	return np.exp(z)/(1.0 + np.exp(z))**2

net = Network([784, 49 ,10])








