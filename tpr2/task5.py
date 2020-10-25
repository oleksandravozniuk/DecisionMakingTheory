import numpy as np

from calculations import get_sigmas
from task1 import pareto


def make_psi_matrix(input_matrix):  # псі матриця
    for i in range(20):
        a = input_matrix[i]  # кожен рядок відсортувати за спаданням значень критеріїв
        a[::-1].sort()
        input_matrix[i] = a
    return input_matrix


def podinovskiy(input_matrix):  # знаходження відношення подиновського
    psi_matrix = make_psi_matrix(input_matrix)
    sigmas = get_sigmas(psi_matrix)  # на основі матриці псі знайти веткори сігма
    res = pareto(sigmas)  # застосувати відношення парето
    return res
