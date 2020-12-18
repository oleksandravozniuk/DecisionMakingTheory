import numpy as np


def association(r, s):
    result = [[0.0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = max(r[i][j], s[i][j])
    return result


def intersection(r, s):
    result = [[0.0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = min(r[i][j], s[i][j])
    return result


def complement(r):
    result = [[0.0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = round(1 - r[i][j], 1)
    return result


def min_values_vector(row, column):
    result = [0] * len(row)
    for i in range(len(row)):
        result[i] = min(row[i], column[i])
    return result


def composition(r, s):
    result = [[0.0] * len(r) for i in range(len(r))]
    r_array = np.array(r)
    s_array = np.array(s)
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = max(min_values_vector(r_array[i], s_array[:, j]))
    return result


def alpha_level(r, alpha):
    result = [[0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            if r[i][j] >= alpha:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result


def strict(r):
    result = [[0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            if r[i][j] > r[j][i]:
                result[i][j] = r[i][j] - r[j][i]
                result[j][i] = 0.0
            else:
                result[j][i] = r[j][i] - r[i][j]
                result[i][j] = 0.0
    return result


def indifference(r):
    result = [[0.0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = round(max(1 - max(r[i][j], r[j][i]), min(r[i][j], r[j][i])), 1)
    return result


def quasi_equivalence(r):
    result = [[0.0] * len(r) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r)):
            result[i][j] = min(r[i][j], r[j][i])
    return result


def reflexivity(r):
    strong = True
    slight = True
    for i in range(len(r)):
        if r[i][i] != 1:
            strong = False
            slight = False
            break
    flag = strong
    if flag:
        for i in range(len(r)):
            for j in range(len(r)):
                if i != j and r[i][j] < 1:
                    continue
                else:
                    strong = False
            for i in range(len(r)):
                for j in range(len(r)):
                    if i != j and r[i][j] <= r[i][i]:
                        continue
                    else:
                        slight = False
    return strong, slight


def antireflexivity(r):
    strong = True
    slight = True
    for i in range(len(r)):
        if r[i][i] != 0:
            strong = False
            slight = False
            break
    flag = strong
    if flag:
        for i in range(len(r)):
            for j in range(len(r)):
                if i != j and r[i][j] > 0:
                    continue
                else:
                    strong = False
            for i in range(len(r)):
                for j in range(len(r)):
                    if i != j and r[i][j] >= r[i][i]:
                        continue
                    else:
                        slight = False
    return strong, slight


def symmetry(r):
    symmetric = True
    for i in range(len(r)):
        for j in range(i, len(r)):
            if r[i][j] != r[j][i]:
                symmetric = False
                break
    return symmetric


def antisymmetry(r):
    antisymmetric = True
    diagonal = []
    for i in range(len(r)):
        diagonal.append(r[i][i])
    if sum(diagonal) > 0:
        antisymmetric = False
    else:
        for i in range(len(r)):
            for j in range(i + 1, len(r)):
                if min(r[i][j], r[j][i]) != 0:
                    antisymmetric = False
    return antisymmetric


def asymmetry(r):
    asymmetric = True
    for i in range(len(r)):
        for j in range(i, len(r)):
            if min(r[i][j], r[j][i]) != 0:
                asymmetric = False
    return asymmetric


def connectivity(r):
    strong = True
    slight = True
    for i in range(len(r)):
        for j in range(i, len(r)):
            if max(r[i][j], r[j][i]) != 1:
                strong = False
                break
    for i in range(len(r)):
        for j in range(i, len(r)):
            if max(r[i][j], r[j][i]) > 0:
                continue
            else:
                slight = False
                break
    return strong, slight


def transitivity(r):
    transitive = True
    for i in range(len(r)):
        for j in range(len(r)):
            for k in range(len(r)):
                if r[i][k] >= min(r[i][j], r[j][k]):
                    continue
                else:
                    transitive = False
    return transitive
