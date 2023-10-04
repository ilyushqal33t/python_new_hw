# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

class Matrix:

    def __init__(self, matrix_list: list):
        self.matrix = matrix_list

    def matrix_transposition(self):
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]


matrix = Matrix([[2, 3, 1], [5, 4, 6]])
print(matrix.matrix)
matrix.matrix_transposition()
print(matrix.matrix)