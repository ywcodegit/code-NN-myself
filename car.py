import numpy as np
class car():
    def __init__(self)：
        self.input = np.zeros((1, 8))
        self.layer1 = np.random.random((8, 16))
        self.modify1 = np.random.random((1, 16))
        self.layer2 = np.random.random((16, 2))
        self.modify2 = np.random.random((1, 2))
        self.output = np.zeros((1, 2))

    def drive():
        step1 = self.input.dot(self.layer1)
        step1 += self.modify1

        step2 = step1.dot(self.layer2)
        step2 += self.modify2

        self.output = step2

cars = []
for i in range(100):
    cars.append(car(??))
