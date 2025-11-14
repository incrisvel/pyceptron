class Pyceptron:
    def __init__(self, learning_rate=0.1, epochs=1):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None