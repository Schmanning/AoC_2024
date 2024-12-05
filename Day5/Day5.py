# Imports
import time, numpy as np

# Zeit Start
start = time.time()


# Functions
def convert_list_to_ints(s: str, sep: str) -> list:
    new_str = [(r.split(sep)) for r in s.split("\n")]
    return [[int(item) for item in row] for row in new_str]


# Main
rules, pr = open("C:/dev/AdventOfCode/2024/Day5/input.txt", "r").read().split("\n\n")
rules = convert_list_to_ints(rules, "|")
pr = convert_list_to_ints(pr, ",")

result1 = 0
result2 = 0

incorrect_orders = []

for pr_line in pr:
    line_correct = True

    for r_line in rules:

        if all(item in pr_line for item in r_line) and pr_line.index(r_line[0]) > pr_line.index(r_line[1]): 
            line_correct = False
            incorrect_orders.append(pr_line)
            break
            
    if line_correct:
        result1 += pr_line[int(len(pr_line) / 2)]



for pr_line in incorrect_orders:
    line_correct = False
    safety_counter = 1000

    while line_correct == False and safety_counter > 0:
        no_errors_found = True

        for r_line in rules:

            if all(item in pr_line for item in r_line) and pr_line.index(r_line[0]) > pr_line.index(r_line[1]):
                pos1, pos2 = pr_line.index(r_line[0]), pr_line.index(r_line[1])
                pr_line[pos1], pr_line[pos2] = pr_line[pos2], pr_line[pos1]
                safety_counter -= 1
                no_errors_found = False
            
            if r_line == rules[-1] and no_errors_found == True:
                line_correct = True
                result2 += pr_line[int(len(pr_line) / 2)]


 
print("Part 1:\t", result1)
print("Part 2:\t", result2)


ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.297s