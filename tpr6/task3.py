import numpy as np

from task1 import min_values_vector, strict


def multiple_expert_decision(m1, m2, m3, m4, m5, weights):
    mp = np.empty((len(m1), len(m1)))
    mq = np.empty((len(m1), len(m1)))
    pmax_values = []
    pnd_values = []
    qmax_values = []
    qnd_values = []
    opt = []
    for i in range(len(m1)):
        for j in range(len(m1)):
            mp[i][j] = min(m1[i][j], m2[i][j], m3[i][j], m4[i][j], m5[i][j])
    mps = np.array(strict(mp))
    for i in range(len(m1)):
        pmax_values.append(max(mps[:, i]))
    for i in range(len(m1)):
        pnd_values.append(1 - pmax_values[i])
    e1 = weights[0] * np.array(m1)
    e2 = weights[1] * np.array(m2)
    e3 = weights[2] * np.array(m3)
    e4 = weights[3] * np.array(m4)
    e5 = weights[4] * np.array(m5)
    for i in range(len(m1)):
        for j in range(len(m1)):
            mq[i][j] = e1[i][j] + e2[i][j] + e3[i][j] + e4[i][j] + e5[i][j]

    mqs = np.array(strict(mq))
    for i in range(len(m1)):
        qmax_values.append(max(mqs[:, i]))
    for i in range(len(mqs)):
        qnd_values.append(1 - qmax_values[i])
    pqnd = min_values_vector(pnd_values, qnd_values)
    for i in range(len(pqnd)):
        if pqnd[i] == max(pqnd):
            opt.append(i + 1)
    range_of_alt = np.argsort(pqnd)
    range_of_alt = range_of_alt[::-1]
    range_of_opt = np.sort(opt)
    range_of_opt = range_of_opt[::-1]
    print()
    print("Ранжування:")
    for i in range_of_alt:
        print(i + 1, end=' ')
    print()
    if len(opt) > 1:
        print("Найбільш переважні альтернативи:")
        for i in range_of_opt:
            print(i, end=' ')
    else:
        print("Найбільш переважна альтернатива:")
        print(opt[0])
    print()
    print("MpqND:")
    for i in pqnd:
        print(i, end=' ')
