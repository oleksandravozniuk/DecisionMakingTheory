import numpy as np
from optimization import part_I, part_P, part_N
from task1 import pareto


# {k4,k6,k8,k11} < {k3,k7,k10,k12} < {k1,k2,k5,k9}
def set_classes(a):
    class_1 = np.array([0, 0, 0, a[3], 0, a[5], 0, a[7], 0, 0, a[10], 0])
    class_2 = np.array([0, 0, a[2], 0, 0, 0, a[6], 0, 0, a[9], 0, a[11]])
    class_3 = np.array([a[0], a[1], 0, 0, a[4], 0, 0, 0, a[8], 0, 0, 0])
    return class_1, class_2, class_3


def div_vectors_into_classes(sigma_vectors):  # розділити критерії на класи
    vectors_matrix = np.array(sigma_vectors)
    class1_matrix = [[0] * 20 for i in range(20)]
    class2_matrix = [[0] * 20 for i in range(20)]
    class3_matrix = [[0] * 20 for i in range(20)]
    for i in range(0, 20):
        for j in range(0, 20):
            a = vectors_matrix[i][j]
            class1_matrix[i][j], class2_matrix[i][j], class3_matrix[i][j] = set_classes(a)

    return class1_matrix, class2_matrix, class3_matrix


def berezovskiy(_sigmas):  # відношення березовського
    it_p_1 = [[0] * 20 for i in range(20)]
    it_i_1 = [[0] * 20 for i in range(20)]
    it_n_1 = [[0] * 20 for i in range(20)]

    berezovskiy_arr = np.empty((20, 20))
    class1, class2, class3 = div_vectors_into_classes(_sigmas)  # розподілити критерії за класами
    pareto1 = np.array(pareto(class1))
    pareto2 = np.array(pareto(class2))
    pareto3 = np.array(pareto(class3))
    # симетрична, асиметрична та непорівнювана частина відношення Парето для класу 1
    i1 = part_I(pareto1)
    p1 = part_P(pareto1)
    n1 = part_N(pareto1)
    # симетрична та асиметрична частина відношення Парето для класу 2
    i2 = part_I(pareto2)
    p2 = part_P(pareto2)
    # симетрична та асиметрична частина відношення Парето для класу 3
    i3 = part_I(pareto3)
    p3 = part_P(pareto3)

    for i in range(0, len(berezovskiy_arr)):
        for j in range(0, len(berezovskiy_arr)):
            if p2[i][j] == 1 and p2[i][j] == p1[i][j]:
                it_p_1[i][j] = 1
            if p2[i][j] == 1 and p2[i][j] == n1[i][j]:
                it_p_1[i][j] = 1
            if i2[i][j] == 1 and i2[i][j] == p1[i][j]:
                it_p_1[i][j] = 1
            if p2[i][j] == 1 and p2[i][j] == i1[i][j]:
                it_p_1[i][j] = 1
            if i2[i][j] == 1 and i2[i][j] == i1[i][j]:
                it_i_1[i][j] = 1
    for i in range(0, len(berezovskiy_arr)):
        for j in range(0, len(berezovskiy_arr)):
            if it_p_1[i][j] == 0 and it_i_1[i][j] == 0:
                it_n_1[i][j] == 1

    for i in range(0, len(berezovskiy_arr)):
        for j in range(0, len(berezovskiy_arr)):
            if p3[i][j] == 1 and p3[i][j] == it_p_1[i][j]:
                berezovskiy_arr[i][j] = 1
            if p3[i][j] == 1 and p3[i][j] == it_n_1[i][j]:
                berezovskiy_arr[i][j] = 1
            if i3[i][j] == 1 and i3[i][j] == it_p_1[i][j]:
                berezovskiy_arr[i][j] = 1
            if p3[i][j] == 1 and p3[i][j] == it_i_1[i][j]:
                berezovskiy_arr[i][j] = 1
    return berezovskiy_arr
