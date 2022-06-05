from abc import ABC, abstractmethod


class Cell():
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

    def __add__(self, addition):
        return Cell(self.size + addition.size)

    def __sub__(self, subtraction):
        result = self.size - subtraction.size
        if result > 0:
            return Cell(result)
        else:
            print("Impossible operation")

    def __mul__(self, multiply):
        return Cell(self.size * multiply.size)

    def __truediv__(self, division):
        if division.size == 0:
            print("Impossible operation")
        else:
            return Cell(self.size / division.size)

    def make_order(self, row_size):
        result = ""
        for i in range(self.size):
            result += "*"
            if (i + 1) % row_size == 0:
                result += "\n"
        return result


cell1 = Cell(12)
cell2 = Cell(3)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell1 = cell1 + cell2
print(cell1.make_order(5))
