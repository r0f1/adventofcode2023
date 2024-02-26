from pathlib import Path
import numpy as np

lines = [[int(n) for n in l.split()] for l in Path("input.txt").read_text().splitlines()]

for part_2 in [False, True]:
    s = 0
    for line in lines:
        if part_2:
            line = line[::-1]
        arr = np.array(line)

        while np.count_nonzero(arr) != 0:
            s += arr[-1]
            arr = np.diff(arr)
    print(s)
