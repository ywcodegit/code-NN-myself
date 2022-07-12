import numpy as np
class car():
    def __init__(self, vector)：
        self.input = np.zeros((8, 1))
        self.layer1 = vector[:128].reshape((16, 8))
        self.modify1 = vector[128: 144]
        self.layer2 = vector[144: 176].reshape((2, 16))
        self.modify2 = vector[176:]
        self.output = np.zeros((1, 2))

    def drive():
        step1 = self.layer1.dot(self.input)
        step1 += self.modify1

        step2 = self.layer2.dot(step1)
        step2 += self.modify2

        self.output = step2

cars = []
for i in range(100):
    cars.append(car(np.random.random((178, 1))))
