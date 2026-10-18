import math


class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def forward(self, inp):
        self.x = 0
        for i in range(len(inp)):
            self.x += inp[i] * self.weights[i]
        self.x += self.weights[-1]
        return math.tanh(self.x)


class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, inp):
        out = []
        for i in range(len(self.neurons)):
            out.append(self.neurons[i].forward(inp))
        return out


class Mlp:
    def __init__(self, weights):
        self.weights = weights
        self.architecture = [79, 64, 32, 1]
        self.layers = []
        iterator = 0
        for i in range(len(self.architecture) - 1):
            self.inpcount = self.architecture[i]
            self.neuroncount = self.architecture[i + 1]

            neurons = []
            for j in range(self.neuroncount):
                neurons.append(Neuron(weights[iterator:(iterator + self.neuroncount + 1)]))

                iterator += self.inpcount + 1
            self.layers.append(Layer(neurons))

    def calculate(self, inp):
        self.out = []
        for i in range(len(self.layers)):
            inp = self.layers[i].forward(inp)
        return inp

    def get_size(self):
        size = 0
        for i in range(len(self.architecture)):
            size += self.architecture[i] * self.architecture[i - 1] + self.architecture[i]
        return size






