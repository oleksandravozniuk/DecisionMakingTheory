from input import expert1, expert2, expert3, expert4, expert5, weights
from output import print_task1, print_properties
from task2 import one_expert_decision
from task3 import multiple_expert_decision

print_task1(expert1, expert2)
print_properties(expert1, expert2)
one_expert_decision(expert1)
multiple_expert_decision(expert1, expert2, expert3, expert4, expert5, weights)
