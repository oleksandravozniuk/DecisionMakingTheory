import numpy as np

# k10>k6>k1>k8>k7>k11>k5>k12>k4>k9>k3>k2
def lexicographic(_sigmas):  # лексикографічне відношення
    sigmas = get_sorted_sigma_by_criteria(_sigmas, [9, 5, 0, 7, 6, 10, 4, 11, 3, 8, 2, 1])  # матриця векторів сігма (стовці відсортовані за критеріями згідно умови)
    lexicographic_arr = np.zeros((20, 20))  # створюємо матрицю відношення
    for i in range(20):
        for j in range(20):
            for k in range(12):
                if sigmas[i][j][k] == 1:
                    lexicographic_arr[i][j] = 1  # належить відношенню якщо 1 і перед не було -1
                    break
                else:
                    if sigmas[i][j][k] == -1 or (k == 11 and sigmas[i][j][k] == 0):  # не належить відношенню якщо перший елемент -1 або останній 0 без 1 у векторі
                        lexicographic_arr[i][j] = 0
                        break
    return lexicographic_arr


def get_sorted_sigma_by_criteria(_sigmas, criteria_order):
    new_sigmas = np.empty((20, 20, 12))  # нова матриця векторів сігма де критерії відсортовані
    for i in range(20):
        for j in range(20):
            new_sigmas[i][j] = set_right_criteria_order(_sigmas[i][j], criteria_order)
    return new_sigmas


def set_right_criteria_order(arr, criteria_order):
    new_arr = np.empty(12)
    for i in range(12):
        index = criteria_order[i]
        new_arr[i] = arr[index]
    return new_arr
