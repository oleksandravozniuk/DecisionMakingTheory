import numpy as np
from file_manager import get_input


def get_sigmas(matrix):
    sigmas = np.empty((20, 20, 12))  # матриця векторів сігма
    for i in range(20):
        for j in range(20):
            arr = np.zeros(12, dtype=int)
            for k in range(12):
                if matrix[i][k] > matrix[j][k]:
                    arr[k] = 1
                else:
                    if matrix[i][k] < matrix[j][k]:
                        arr[k] = -1
            sigmas[i][j] = arr
    return sigmas