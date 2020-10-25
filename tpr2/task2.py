import numpy as np


def majoritar(sigmas):
    majoritar_arr = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            if np.sum(sigmas[i][j]) > 0:
                majoritar_arr[i][j] = 1
    return majoritar_arr
