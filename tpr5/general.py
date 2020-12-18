

def normalize_weights(weights):
    sum_weights = sum(weights)
    normalized_weights = []
    for i in range(0,len(weights)):
        normalized_weights.append(weights[i]/sum_weights)
    return normalized_weights

# множення матриці на матрицю ваг критеріїв
def weighted_estimates(r_matrix, weights):
    norm_weights = normalize_weights(weights)
    for i in range(0, 15):
        for j in range(0, 12):
            r_matrix[i][j] = r_matrix[i][j] * norm_weights[j]
    return r_matrix

# виведення результатів
def output_result(result, opt, method):
    print(method)
    print("Range:")
    for i in result:
        print(i, end=" ")
    print()
    if len(opt)==1:
        print("The best alternative:")
    else:
        print("Best alternatives:")
    for i in opt:
        print(i, end=" ")
    print()


