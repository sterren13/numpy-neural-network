from Stage import Stage
import numpy as np

class Activation(Stage):
    def forward(self, x):
        raise NotImplementedError()

    def backward(self, dvalues):
        raise NotImplementedError()

    def update(self, learning_rate):
        pass


class Sigmoide(Activation):
    def forward(self, x):
        pass

    def backward(self, dvalues):
        pass