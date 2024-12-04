# Imports
import time, numpy as np

# Zeit Start
start = time.time()


def rotate_45(m: np.array, clock_wise = True):
    row, col = len(m), len(m[0])
    size_n = row + col - 1
    rotated = [[] for _ in range(size_n)]

    for i in range(row):
        for j in range(col):
            if clock_wise:
                rotated[i + j].append(m[i, j])
            else:
                rotated[i - j + (row - 1)].append(m[i, j])
    
    max_len = max(len(r) for r in rotated)
    re = np.array([r + [0] * (max_len - len(r)) for r in rotated])
    row_strings = [" ".join(map(str, row)).replace("0", "").replace(" ", "") for row in re]
    return row_strings


def count_mat(mat: list):
    res = 0
    for row in mat:
        res += row.count("XMAS")
        res += row.count("SAMX")
    return res


def check_cross(file: list, row: int, col: int):
    c = file[row-1][col-1] + "A" + file[row+1][col+1]
    d = file[row+1][col-1] + "A" + file[row-1][col+1]

    if c not in ("MAS", "SAM") or d not in ("MAS", "SAM"):
        return 0
    return 1


# Main
file = [s.replace("\n", "").replace(" ", "") for s in open("C:/dev/AdventOfCode/2024/Day4/input.txt", "r").readlines()]

f = np.array([list(row) for row in file])
f_transposed = [" ".join(map(str, row)).replace(" ", "") for row in f.T]
f_45_clock, f_45_counter = rotate_45(f), rotate_45(f, False)

result = count_mat(file) + count_mat(f_transposed) + count_mat(f_45_clock) + count_mat(f_45_counter)

result2 = 0

for i in range(1, len(file) - 1):
    for j in range(1, len(file[0]) - 1):
        if file[i][j] == "A":
            result2 += check_cross(file, i, j)

print("Part 1:\t", str(result))
print("Part 2:\t", str(result2))


ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.036s