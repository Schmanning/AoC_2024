# Imports
import time

# Zeit Start
start = time.time()

# Main
f = open("C:/dev/AdventOfCode/2024/Day2/input.txt", "r").readlines()


def check_safe(line: list):
    ascending = line[0] < line[1]

    for j in range(len(line) - 1):
        if abs(line[j] - line[j+1]) > 3 or \
            (ascending == True and line[j] >= line[j+1]) or \
                (ascending == False and line[j] <= line[j+1]):
            return 0
    return 1


safe_count = 0

for i in range(len(f)):
    current_line = [int(x) for x in f[i].replace("\n", "").split(" ")]
    safe_count += check_safe(current_line)

print(safe_count)


ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s