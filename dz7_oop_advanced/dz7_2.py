from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculate_fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calculate_fabric(self):
        return 2 * self.height + 0.3


suit = Suit(180)
coat = Coat(52)
print(f"Suit fabric:{suit.calculate_fabric}")
print(f"Coat fabric:{coat.calculate_fabric}")
