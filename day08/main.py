from math import lcm
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

d = {}
for line in lines[2:]:
    s, ts = line.split(" = ")
    d[s] = {"L": ts[1:4], "R": ts[6:9]}

def calc(curr):
    counter = 0
    while not curr.endswith("Z"):
        for k in lines[0]:
            curr = d[curr][k]
        counter += len(lines[0])
    return counter

nodes = sorted(n for n in d.keys() if n.endswith("A"))
paths = [calc(c) for c in nodes]
print(paths[0])
print(lcm(*paths))
