class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for row in self.matrix:
            for column in row:
                result += str(column) + " "
            result += "\n"
        return result

    def __add__(self, added_matrix):
        new_matrix = list(self.matrix);
        for i, row in enumerate(new_matrix):
            for j, column in enumerate(row):
                new_matrix[i][j] = column + added_matrix.matrix[i][j]
        return Matrix(new_matrix)


m1 = Matrix([[34, 34, 4], [4, 65, 5]])
print(m1)
m2 = Matrix([[1, 2, 3], [5, 6, 7]])
print(m2)
print(m1 + m2)
