from itertools import combinations
from pathlib import Path
import re

import numpy as np

lines = Path("input.txt").read_text().splitlines()

y_offsets = []
counter = 0
for y, line in enumerate(lines):
    if line.find("#") < 0:
       counter += 1_000_000 - 1
    y_offsets.append(y+counter)

lines_T = np.transpose(np.array([list(line) for line in lines]))
lines_T = ["".join(line) for line in lines_T]

x_offsets = []
counter = 0
for x, line in enumerate(lines_T):
    if line.find("#") < 0:
        counter += 1_000_000 - 1
    x_offsets.append(x+counter)

points = []
for y, line in enumerate(lines):
    res = [i.start() for i in re.finditer("#", line)]
    for x in res:
        points.append((x_offsets[x], y_offsets[y]))

print(sum(abs(x1-x2) + abs(y1-y2) for (x1, y1), (x2, y2) in combinations(points, r=2)))
