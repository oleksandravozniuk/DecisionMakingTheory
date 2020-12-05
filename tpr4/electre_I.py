from itertools import groupby

import numpy as np

from input import alternatives, weights, c, d


def count_diff_ai_bi(alternatives_matrix, weights_array):
    alt = np.array(alternatives_matrix)
    weights = np.array(weights_array)
    diffs_ai_bi = []
    for i in range(0, len(alt[0, :])):
        diffs_ai_bi.append(weights[i] * (np.amax(alt[:, i]) - np.amin(alt[:, i])))
    return diffs_ai_bi


def sum_ij(a1, a2, weights_array):
    result_sum = 0
    for i in range(0, len(a1)):
        if a1[i] >= a2[i]:
            result_sum += weights_array[i]
    return result_sum


def c_matrix(alternatives_matrix, weights_array):
    result_matrix = [[0] * 15 for i in range(15)]
    weights_sum = np.sum(weights_array)
    for i in range(0, 15):
        for j in range(0, 15):
            if i != j:
                result_matrix[i][j] = sum_ij(alternatives_matrix[i], alternatives_matrix[j],
                                             weights_array) / weights_sum
    return result_matrix


def d_ij(a1, a2, weights_array, diffs_ai_bi):
    diffs = []
    selected_diffs_ai_bi = []
    for i in range(0, len(a1)):
        if a1[i] < a2[i]:
            diffs.append(weights_array[i] * (a2[i] - a1[i]))
            selected_diffs_ai_bi.append(diffs_ai_bi[i])
    try:
        return np.amax(diffs) / np.amax(selected_diffs_ai_bi)
    except:
        return 0


def d_matrix(alternatives_matrix, weights_array):
    result_matrix = [[1] * 15 for i in range(15)]
    diffs_ai_bi = count_diff_ai_bi(alternatives_matrix, weights_array)
    for i in range(0, 15):
        for j in range(0, 15):
            if i != j:
                result_matrix[i][j] = d_ij(alternatives_matrix[i], alternatives_matrix[j], weights_array, diffs_ai_bi)
    return result_matrix


def write_to_file(filename, matrix, formated):
    f = open(filename, "w")
    if formated:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                f.write("{:.3f} ".format(matrix[i][j]))
            f.write('\n')
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                f.write(" {} ".format(matrix[i][j]))
            f.write('\n')
    f.close()


def electre_I(alternatives_matrix, weights_array, c, d):
    C_matrix = np.array(c_matrix(alternatives_matrix, weights_array))
    D_matrix = np.array(d_matrix(alternatives_matrix, weights_array))
    relation_matrix = [[0] * 15 for i in range(15)]
    write_to_file("c.txt", C_matrix, True)
    write_to_file("d.txt", D_matrix, True)
    R = []
    X = []
    for i in range(0, len(C_matrix)):
        for j in range(0, len(C_matrix)):
            if i != j and C_matrix[i][j] >= c and D_matrix[i][j] <= d:
                relation_matrix[i][j] = 1
                R.append([i, j])
    write_to_file("relations.txt", relation_matrix, False)
    for i in range(0, 15):
        flag = True
        for j in range(0, len(R)):
            if i in R[j]:
                flag = False
                break
        if flag:
            X.append(i)
    for i in range(0, len(R)):
        pair = R[i]
        x_candidate = pair[0]
        flag = True
        for j in range(0, len(R)):
            pair_compare = R[j]
            if pair_compare[1] == x_candidate:
                flag = False
                break
        if flag:
            X.append(x_candidate)
    X.sort()
    X_result = [el for el, _ in groupby(X)]
    for i in range(0, len(X_result)):
        X_result[i] = X_result[i] + 1
    return X_result


print("X*: {}".format(electre_I(alternatives, weights, c, d)))
