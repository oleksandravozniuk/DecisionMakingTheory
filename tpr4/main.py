from electre_I import electre_I
from input import alternatives, weights

# electre_I(alternatives, weights, 0.5, 0.1)
# electre_I(alternatives, weights, 0.5, 0.2)
# electre_I(alternatives, weights, 0.5, 0.3)
# electre_I(alternatives, weights, 0.5, 0.4)
# electre_I(alternatives, weights, 0.5, 0.5)

# print("X*: {}".format(electre_I(alternatives, weights, 0.5, 0.49)))
# print("X*: {}".format(electre_I(alternatives, weights, 0.6, 0.49)))
# print("X*: {}".format(electre_I(alternatives, weights, 0.7, 0.49)))
# print("X*: {}".format(electre_I(alternatives, weights, 0.8, 0.49)))
# print("X*: {}".format(electre_I(alternatives, weights, 0.9, 0.49)))
# print("X*: {}".format(electre_I(alternatives, weights, 1, 0.49)))

print("X*: {}".format(electre_I(alternatives, weights, 1, 0.01)))
print("X*: {}".format(electre_I(alternatives, weights, 0.9, 0.1)))
print("X*: {}".format(electre_I(alternatives, weights, 0.8, 0.2)))
print("X*: {}".format(electre_I(alternatives, weights, 0.7, 0.3)))
print("X*: {}".format(electre_I(alternatives, weights, 0.6, 0.4)))
print("X*: {}".format(electre_I(alternatives, weights, 0.5, 0.49)))