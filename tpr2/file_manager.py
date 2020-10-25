import numpy as np


def get_input():
    return np.loadtxt("var5_input.txt", dtype=int)


def write_number(number):
    f = open("Var-05-ВознюкОлександра.txt", "a")
    f.write(" {} ".format(number))
    f.write('\n')
    f.close()


def write_matrix(matrix):
    f = open("Var-05-ВознюкОлександра.txt", "a")
    for i in range(20):
        for j in range(20):
            f.write(" {} ".format(int(matrix[i][j])))
        f.write('\n')
    f.close()
