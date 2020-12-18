import numpy as np

from task1 import strict


def one_expert_decision(r):
    mrs = np.array(strict(r))
    max_values = []
    nd_values = []
    opt = []
    for i in range(len(r)):
        max_values.append(max(mrs[:, i]))
    for i in range(len(mrs)):
        nd_values.append(1 - max_values[i])
    for i in range(len(nd_values)):
        if nd_values[i] == max(nd_values):
            opt.append(i + 1)
    range_of_alt = np.argsort(nd_values)
    range_of_alt = range_of_alt[::-1]
    print()
    print("Ранжування:")
    for i in range_of_alt:
        print(i + 1, end=' ')
    print()
    if len(opt) > 1:
        print("Найбільш переважні альтернативи:")
        for i in opt:
            print(i + 1, end=' ')
    else:
        print("Найбільш переважна альтернатива:")
        print(opt[0])
