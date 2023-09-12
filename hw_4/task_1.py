# Напишите функцию для транспонирования матрицы


def matrix_transposition(matrix: list) -> list:
    trnsptn_mtrx = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trnsptn_mtrx


matrix = [[2, 3, 1], [5, 4, 6]]
print(matrix)
print(matrix_transposition(matrix))