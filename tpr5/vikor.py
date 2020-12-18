
import numpy as np

from general import weighted_estimates, output_result


def f_max_min_values(alt):
    alternatives = np.array(alt)
    max_f = []
    min_f = []
    for j in range(0, 12):
        max_f.append(max(alternatives[:, j]))
        min_f.append(min(alternatives[:, j]))
    return max_f, min_f


def make_vikor_matrix(alternatives, max_f, min_f):
    vikor_matrix = np.empty((15, 12))
    for i in range(0, 15):
        for j in range(0, 12):
            vikor_matrix[i][j] = (max_f[j] - alternatives[i][j]) / (max_f[j] - min_f[j])
    return vikor_matrix


def calculate_sk(weighted_vikor_matrix):
    sk = []
    for i in weighted_vikor_matrix:
        sk.append(sum(i))
    max_sk = max(sk)
    min_sk = min(sk)
    return sk, max_sk, min_sk


def calculate_rk(weighted_vikor_matrix):
    rk = []
    for i in weighted_vikor_matrix:
        rk.append(max(i))
    max_rk = max(rk)
    min_rk = min(rk)
    return rk, max_rk, min_rk


def check_c1_c2(q, q_i, sk_i, rk_i):
    check_c1 = False
    check_c2 = False
    if q[1] - q[0] >= 1 / 14:
        check_c1 = True
    if q_i[0] == sk_i[0] or q_i[0] == rk_i[0]:
        check_c2 = True
    return check_c1, check_c2


def vikor(alternatives,weights, v):
    max_f, min_f = f_max_min_values(alternatives)
    vikor_matrix = make_vikor_matrix(alternatives, max_f, min_f)
    weighted_vikor_matrix = weighted_estimates(vikor_matrix, weights)
    sk, max_sk, min_sk = calculate_sk(weighted_vikor_matrix)
    rk, max_rk, min_rk = calculate_rk(weighted_vikor_matrix)
    q = []
    for i in range(0, 15):
        q.append(v * (sk[i] - min_sk) / (max_sk - min_sk) + (1 - v) * (rk[i] - min_rk) / (max_rk - min_rk))
    q_indexes = np.argsort(q)
    sk_indexes = np.argsort(sk)
    rk_indexes = np.argsort(rk)
    print("Range Q:")
    for i in q_indexes:
        print(i + 1, end=" ")
    print()
    print("Range S")
    for i in sk_indexes:
        print(i + 1, end=" ")
    print()
    print("Range R")
    for i in rk_indexes:
        print(i + 1, end=" ")
    print()
    q_sorted = sorted(q)
    check_c1, check_c2 = check_c1_c2(q, q_indexes, sk_indexes, rk_indexes)
    opt = []
    opt_values = []
    if check_c1 == True and check_c2 == True:
        opt.append(q_indexes[0] + 1)
        opt_values.append(q[0])
    elif check_c1 == False and check_c2 == True:
        print("С1 is not satisfied")
        print()
        opt.append(q_indexes[0] + 1)
        opt_values.append(q[0])
        for i in range(1, len(q)):
            if q[i] - q[i - 1] < 1 / 14:
                opt.append(q_indexes[i] + 1)
                opt_values.append(q[i])
            else:
                break
    elif check_c1 == True and check_c2 == False:
        print("С2 is not satisfied")
        print()
        opt.append(q_indexes[0] + 1)
        opt_values.append(q[0])
        opt.append(q_indexes[1] + 1)
        opt_values.append(q[1])
    else:
        print("С1 and С2 are not satisfied")
        print()
    for i in range(0, len(q_indexes)):
        q_indexes[i] += 1
    return q_indexes, opt, opt_values


def print_vikor(alternatives,weights):
    result, opt, opt_values = vikor(alternatives,weights, 0.5)
    output_result(result, opt, "VIKOR (v = 0.5)")
    print("Best Q:")
    for i in opt_values:
        print(i, end=' ')
    print()
    print("Changing v")
    print(".............................................................")
    v_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for v in v_values:
        result, opt, opt_values = vikor(alternatives,weights, v)
        output_result(result, opt, "VIKOR ( v = {})".format(v))
        print("Best Q:")
        for i in opt_values:
            print(i, end=' ')
        print()
        print("................................................................")


