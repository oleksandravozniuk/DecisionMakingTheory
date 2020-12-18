import math
import numpy as np

from general import output_result, weighted_estimates


def norm_astimates(alternatives):
    r_matrix = [[0] * 12 for i in range(15)]
    a = np.array(alternatives)
    pows = []
    for k in range(0, 12):
        column = a[:, k]
        for i in column:
            i = pow(i, 2)
        pows.append(sum(column))
    for i in range(0, 15):
        for j in range(0, 12):
            r_matrix[i][j] = alternatives[i][j] / (math.sqrt(pows[j]))
    return r_matrix


def norm_astimates_for_kplus_kminus(alt):
    alternatives = np.array(alt)
    kplus_criteria = np.empty((15, 7))
    kminus_criteria = np.empty((15, 5))
    r_matrix = np.empty((15, 12))
    for i in range(0, 15):
        for j in range(0, 7):
            kplus_criteria[i][j] = alternatives[i][j]
    for i in range(0, 15):
        for j in range(7, 12):
            kminus_criteria[i][j - 7] = alternatives[i][j]
    for i in range(0, 15):
        for j in range(0, 7):
            min_kplus = min(kplus_criteria[:, j])
            max_kplus = max(kplus_criteria[:, j])
            kplus_criteria[i][j] = (kplus_criteria[i][j] - min_kplus) / (max_kplus - min_kplus)
    for i in range(0, 15):
        for j in range(0, 5):
            min_kminus = max(kminus_criteria[:, j])
            max_kminus = min(kminus_criteria[:, j])
            kminus_criteria[i][j] = (min_kminus - kminus_criteria[i][j]) / (min_kminus - max_kminus)
    for i in range(0, 15):
        for j in range(0, 7):
            r_matrix[i][j] = kplus_criteria[i][j]
    for i in range(0, 15):
        for j in range(7, 12):
            r_matrix[i][j] = kminus_criteria[i][j - 7]
    return r_matrix


def pis_nis(row_i, max_j, min_j):
    r_pis = []
    r_nis = []
    for i in range(0, len(row_i)):
        r_pis.append(pow((row_i[i] - max_j[i]), 2))
        r_nis.append(pow((row_i[i] - min_j[i]), 2))
    d_pis = math.sqrt(sum(r_pis))
    d_nis = math.sqrt(sum(r_nis))
    return d_pis, d_nis


def find_c(d_pis, d_nis):
    c = []
    for i in range(0, len(d_pis)):
        c.append(d_nis[i] / (d_pis[i] + d_nis[i]))
    return c


def topsis(alternatives, weights, task):
    if task == "a":
        norm_a = norm_astimates(alternatives)
    else:
        norm_a = norm_astimates_for_kplus_kminus(alternatives)
    weighted_a = np.array(weighted_estimates(norm_a, weights))
    max_j = []
    min_j = []
    for j in range(0, 12):
        max_j.append(max(weighted_a[:, j]))
        min_j.append(min(weighted_a[:, j]))
    d_pis = []
    d_nis = []
    for i in range(0, 15):
        d_p, d_n = pis_nis(weighted_a[i], max_j, min_j)
        d_pis.append(d_p)
        d_nis.append(d_n)
    c = find_c(d_pis, d_nis)
    indexes = np.argsort(c)
    for i in range(0, len(indexes)):
        indexes[i] += 1
    result = indexes[::-1]
    opt = [result[0]]
    return result, opt


def print_topsis(alternatives, weights):
    resultA, optA = topsis(alternatives, weights, "a")
    resultB, optB = topsis(alternatives, weights, "b")
    output_result(resultA, optA, "TOPSIS (task a)")
    print(".................................................")
    output_result(resultB, optB, "TOPSIS (task b)")
