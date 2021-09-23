import random
from typing import Tuple


class RandomParameters:
    def __init__(self, seed) -> None:
        random.seed(seed)

    @staticmethod
    def activation():
        activation_layers = [
            "relu",
            "sigmoid",
            "softmax",
            "softplus",
            "softsign",
            "tanh",
            "selu",
            "elu",
            "exponential",
        ]
        number = random.randint(1, len(activation_layers))
        return activation_layers[number]

    @staticmethod
    def filter_size():
        number = random.randint(1, 5)
        return (number, number)

    @staticmethod
    def first_filter() -> int:
        return random.randint(1, 64)

    @staticmethod
    def second_filter() -> int:
        number = random.randint(5, 10)
        return (number, number)

    @staticmethod
    def third_filter() -> int:
        number = random.randint(10, 15)
        return (number, number)

    @staticmethod
    def dropout():
        return random.uniform(0.1, 0.8)


if __name__ == "__main__":
    studentnr = 104648
    R = RandomParameters(studentnr)
    print(R.activation())
