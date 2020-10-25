from calculations import get_sigmas
from file_manager import get_input, write_number, write_matrix
from optimization import print_opt
from task1 import pareto
from task2 import majoritar
from task3 import lexicographic
from task4 import berezovskiy
from task5 import podinovskiy

input_matrix = get_input()

print(pareto(get_sigmas(input_matrix)))
print_opt(pareto(get_sigmas(input_matrix)))
write_number(1)
write_matrix(pareto(get_sigmas(input_matrix)))

print(majoritar(get_sigmas(input_matrix)))
print_opt(majoritar(get_sigmas(input_matrix)))
write_number(2)
write_matrix(majoritar(get_sigmas(input_matrix)))

print(lexicographic(get_sigmas(input_matrix)))
print_opt(lexicographic(get_sigmas(input_matrix)))
write_number(3)
write_matrix(lexicographic(get_sigmas(input_matrix)))

print(berezovskiy(get_sigmas(input_matrix)))
print_opt(berezovskiy(get_sigmas(input_matrix)))
write_number(4)
write_matrix(berezovskiy(get_sigmas(input_matrix)))

print(podinovskiy(input_matrix))
print_opt(podinovskiy(input_matrix))
write_number(5)
write_matrix(podinovskiy(input_matrix))
