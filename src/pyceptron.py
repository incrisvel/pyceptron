import random

class Pyceptron:
    def __init__(self, inputs):
        self.learning_rate = 0.1 # ajuste nos pesos em caso de resposta incorreta
        self.epochs = 1 # quantidade de vezes que o modelo vê os dados de treino
        self.weights = {name: 0 for name in inputs} # {nome_campo : peso_inicial}
        self.bias = 0

    def net_input(self, values_dict):
        sum = 0

        for name, value in values_dict.items():
            sum += self.weights[name] * value

        return sum + self.bias

    def activation(self, value):
        return 1 if value > 0 else 0

    def guess(self, data):
        value = self.net_input(data)

        return self.activation(value)

    def train(self, dataset, answers):
        for _ in range(self.epochs):
           for data, correct_answer in zip(dataset, answers):
               guess = self.guess(data)
               diff = correct_answer - guess # cálculo do erro

               for name, weight in self.weights.items():
                    self.weights[name] = weight + self.learning_rate * diff * data[name]

               self.bias += self.learning_rate * diff
