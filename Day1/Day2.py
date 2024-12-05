# Imports
import time, numpy as np

# Zeit Start
start = time.time()

# Main
l1, l2 = (np.sort(arr) for arr in np.array([[int(item) for item in row.split("   ")] for row in open("C:/dev/AdventOfCode/2024/Day1/input.txt", "r").read().split("\n")]).T)
result1 = sum(abs(l1[x] - l2[x]) for x in range(len(l1)))
result2 = sum(l1[x] * np.count_nonzero(l2 == l1[x]) for x in range(len(l1)))

print("Part 1:\t", result1)
print("Part 2:\t", result2)

ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s