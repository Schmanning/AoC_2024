# Imports
import time

# Zeit Start
start = time.time()

# Main
f = open("C:/dev/AdventOfCode/2024/Day3/input.txt", "r").read().replace("\n", "").split("mul(")

result1, result2, instructions_enabled = 0, 0, True

for split in f:
    temp_enabled = instructions_enabled

    if split.rfind("don't()") > split.rfind("do()"):
        instructions_enabled = False
    elif split.rfind("do()") > split.rfind("don't()"):
        instructions_enabled = True

    if not split.__contains__(",") or not split.__contains__(")"):
        continue
    
    split = split.replace(",", " ").replace(")", " ").split(" ")

    if len(split) > 1 and split[0].isdigit() and split[1].isdigit():
        addition = int(split[0]) * int(split[1])
        result1 += addition
        if temp_enabled:
            result2 += addition

print("Part 1:\t", str(result1))
print("Part 2:\t", str(result2))


ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.002s