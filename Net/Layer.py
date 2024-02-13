from Stage import Stage
class Layer(Stage):
    def __init__(self, n_inputs, n_neurons):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons

    def forward(self, x):
        pass

    def backward(self, grad):
        pass

    def update(self, lr):
        pass