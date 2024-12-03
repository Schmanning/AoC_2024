# Imports
import time

# Zeit Start
start = time.time()

# Main
f = open("C:/dev/AdventOfCode/2024/Day2/input.txt", "r").readlines()


def check_safe(line: list) -> int:
    for remove_index in range(len(line)):
        temp_line = line[:remove_index] + line[remove_index+1:]
        ascending = temp_line[0] < temp_line[1]
        report_safe = True

        for j in range(len(temp_line) - 1):
            if abs(temp_line[j] - temp_line[j+1]) > 3 or \
                (ascending == True and temp_line[j] >= temp_line[j+1]) or \
                    (ascending == False and temp_line[j] <= temp_line[j+1]):
                report_safe = False
        
        if report_safe:
            return 1
    return 0


safe_count = 0

for i in range(len(f)):
    current_line = [int(x) for x in f[i].replace("\n", "").split(" ")]
    safe_count += check_safe(current_line)

print(safe_count)


ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.004s