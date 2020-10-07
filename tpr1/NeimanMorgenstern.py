def nm(matrix):
    s_diff = get_s_diff(matrix)
    q_list = []
    for i in range(len(s_diff)):
        q = []
        if (i != 0):
            for l in range(len(q_list[i - 1])):
                q.append(q_list[i - 1][l])
        for j in range(len(s_diff[i])):
            if i == 0:
                q.append(s_diff[i][j])
            else:
                flag = True
                for k in range(len(q_list[i - 1])):
                    if matrix[s_diff[i][j]][q_list[i - 1][k]] == 1:
                        flag = False
                if flag == True:
                    q.append(s_diff[i][j])
        q_list.append(q)
    print(q_list)
    return q_list.pop()


def get_s_diff(matrix):
    s_list = []
    flag = False
    s0 = []
    for i in range(15):
        for j in range(15):
            if matrix[i][j] == 1:
                flag = True
        if flag == False:
            s0.append(i)
        flag = False

    flag = True
    s_list.append(s0)
    k = 0
    step = 0
    while k < 15 - len(s0):
        s = []
        for i in range(15):
            for j in range(15):
                if matrix[i][j] == 1 and not any(el == j for el in s_list[step]):
                    flag = False
            if flag == True:
                s.append(i)
                if not any(el == i for el in s_list[step]):
                    k = k + 1
            flag = True
        s_list.append(s)
        step = step + 1
    print("S: " + str(s_list))
    s_diff = []
    for q in range(len(s_list)):
        s = []
        for r in range(len(s_list[q])):
            if not any(el == s_list[q][r] for el in s_list[q - 1]) or q == 0:
                s.append(s_list[q][r])
        s_diff.append(s)
    print(s_diff)
    return s_diff


def check_inner_persistence(matrix_t, nm_list):
    for k in range(len(nm_list)):
        for j in range(len(nm_list)):
            if nm_list[k] != nm_list[j]:
                if matrix_t[nm_list[k]][nm_list[j]] == 1:
                    return False
    return True


def check_outer_persistence(matrix_t, nm_list):
    all_input = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    not_decisions = list(set(all_input) - set(nm_list))

    for k in range(len(nm_list)):
        flag = False
        for j in range(len(not_decisions)):
            if nm_list[k] != not_decisions[j]:
                if matrix_t[nm_list[k]][not_decisions[j]] == 1:
                    flag = True
        if flag == False:
            return False
    return True
