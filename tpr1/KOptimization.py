import numpy as np

def max_include(matrix):
    include_list = []
    for i in range(15):
        row = matrix[i]
        max = 0
        if(sum(row)!=0):
            for j in range(15):
                if(i!=j):
                    flag = True
                    for k in range(15):
                        if row[k] != matrix[j][k] and matrix[j][k] == 1:
                            flag = False
                    if flag == True:
                        max = max + 1
        include_list.append(max)
    max_incl = np.max(include_list)
    res_list = []
    if max_incl != 0:

        for q in range(15):
            if include_list[q] == max_incl:
                res_list.append(q)
    return res_list



def k1(matrix):
    new_matrix = np.ones((15, 15))
    for i in range(15):
        for j in range(15):
            if(matrix[i][j]!=matrix[j][i]):
                if(matrix[i][j] == 0):
                    new_matrix[i][j] = 0
                else:
                    new_matrix[j][i] = 0
    print(new_matrix)
    print(max_include(new_matrix))

def k2(matrix):
    new_matrix = np.ones((15, 15))
    for i in range(15):
        for j in range(15):
            if (matrix[i][j] != matrix[j][i]):
                if(matrix[i][j]==0):
                    new_matrix[i][j] = 0
                else:
                    new_matrix[j][i] = 0
            else:
                if matrix[i][j] == matrix[j][i] and matrix[i][j] == 1:
                    new_matrix[i][j] = 0
                    new_matrix[j][i] = 0

    print(new_matrix)
    print(max_include(new_matrix))

def k3(matrix):
    new_matrix = np.zeros((15, 15))
    for i in range(15):
        for j in range(15):
            if (matrix[i][j] != matrix[j][i]):
                if (matrix[i][j] == 1):
                    new_matrix[i][j] = 1
                else:
                    new_matrix[j][i] = 1
            else:
                if matrix[i][j] == matrix[j][i] and matrix[i][j] == 1:
                    new_matrix[i][j] = 1
                    new_matrix[j][i] = 1

    print(new_matrix)
    print(max_include(new_matrix))

def k4(matrix):
    new_matrix = np.zeros((15, 15))
    for i in range(15):
        for j in range(15):
            if (matrix[i][j] != matrix[j][i]):
                if (matrix[i][j] == 1):
                    new_matrix[i][j] = 1
                else:
                    new_matrix[j][i] = 1

    print(new_matrix)
    print(max_include(new_matrix))