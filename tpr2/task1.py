import numpy as np


# будуємо відношення парето
def pareto(sigmas):
    pareto_arr = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            flag = True
            for k in range(12):
                if sigmas[i][j][k] == -1:
                    flag = False
            if flag:  # якщо у векторі сігма нема -1
                pareto_arr[i][j] = 1
            else:  # якщо у векторі сігма є -1
                pareto_arr[i][j] = 0
    return pareto_arr
