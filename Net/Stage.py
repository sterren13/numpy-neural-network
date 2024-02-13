
class Stage:
    def forward(self, x):
        raise NotImplementedError()

    def backward(self, grad):
        raise NotImplementedError()

    def update(self, lr):
        raise NotImplementedError()