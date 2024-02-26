# relativistic-turtle on reddit
from pathlib import Path
import numpy as np
from numpy.polynomial.polynomial import Polynomial

lines = [[int(n) for n in l.split()] for l in Path("input.txt").read_text().splitlines()]

answer = [0, 0]
for y in lines:
    poly = Polynomial.fit(np.arange(len(y)), y, deg=len(y)-1)
    answer[0] += round(poly(len(y)))
    answer[1] += round(poly(-1))

print("Part 1: {}\nPart 2: {}".format(*answer))
