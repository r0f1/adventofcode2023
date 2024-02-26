from math import lcm
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

d = {}
for line in lines[2:]:
    s, ts = line.split(" = ")
    d[s] = {"L": ts[1:4], "R": ts[6:9]}

def calc1():
    counter = 0
    curr = "AAA"
    while curr != "ZZZ":
        for k in lines[0]:
            curr = d[curr][k]
        counter += len(lines[0])
    return counter

def calc2(curr):
    counter = 0
    while not curr.endswith("Z"):
        for k in lines[0]:
            curr = d[curr][k]
        counter += len(lines[0])
    return counter

print(calc1())
paths = [calc2(c) for c in d.keys() if c.endswith("A")]
print(lcm(*paths))
