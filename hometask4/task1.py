# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 4], [31, 17, 15]]


def trans_matrix(mtrx: list):
    trans_m = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]
    return trans_m


tr_m = trans_matrix(matrix)
print(tr_m)