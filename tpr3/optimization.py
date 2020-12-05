import numpy as np


def domination_P_max(_matrix):  # найбільші альтернативи по Р (домінування)
    matrix = np.array(_matrix)
    res = []
    for i in range(0, len(matrix)):
        if matrix[i][i] == 0 and matrix[i].sum() == len(matrix) - 1:
            res.append(i + 1)
    return res


def domination_R_max(_matrix):  # найбільші альтернативи по R (домінування)
    matrix = np.array(_matrix)
    res = []
    strong_res = []
    for i in range(0, len(matrix)):
        if matrix[i].sum() == len(matrix):
            res.append(i + 1)
            if matrix[:, i].sum() == 1:
                strong_res.append(i + 1)
    return res, strong_res


def blocking_P_max(_matrix):  # максимальні альтернативи по Р (блокування)
    matrix = np.array(_matrix)
    res = []
    for i in range(0, len(matrix)):
        if matrix[:, i].sum() == 0:
            res.append(i + 1)
    return res


def part_I(_matrix):  # симетрична частина
    return (_matrix == _matrix.T) * _matrix


def part_P(_matrix):  # асиметрична частина
    return _matrix - part_I(_matrix)


def part_N(_matrix):  # частина відношення непорівнюваності
    return (_matrix == _matrix.T) - part_I(_matrix)


def blocking_R_max(_matrix):  # максимальні альтернативи по R (блокування)
    matrix = np.array(_matrix)
    symmetrical = part_I(matrix)
    res = []
    strong_res = []
    for i in range(0, len(matrix)):
        if not np.any(not np.array_equal(matrix[:, i], symmetrical[:, i])):
            res.append(i + 1)
            if matrix[:, i].sum() == 1 and matrix[i][i] == 1:
                strong_res.append(i + 1)
    return res, strong_res


def check_symmetrical_part(_matrix):  # перевіряємо симетричність
    symmetrical = part_I(np.array(_matrix))
    flag = False
    for i in range(0, len(symmetrical)):
        if symmetrical[i].sum() > 0:
            flag = True
            break
    return flag


def print_opt(matrix):  # вивести найбільші або максимальні альтернативи
    if check_symmetrical_part(matrix):
        m, sm = domination_R_max(matrix)
        if len(m) > 0:
            print("Greatest alternatives by R: {}".format(m))
            print("Strong greatest alternatives by R: {}".format(sm))
        else:
            m, sm = blocking_R_max(matrix)
            print("Max alternatives by R: {}".format(m))
            print("Strong max alternatives by R: {}".format(sm))
    else:
        if len(domination_P_max(matrix)) > 0:
            print("Greatest by Р: {}".format(domination_P_max(matrix)))
        else:
            print("Max by Р: {}".format(blocking_P_max(matrix)))
