from collections import defaultdict
import math
import re

with open("input.txt") as f:
    lines = [x.split(":")[1] for x in f]

part1 = 0
part2 = 0

allowed = {"red": 12, "green": 13, "blue": 14}
for idx, content in enumerate(lines, start=1):
    d = defaultdict(int)
    for n, c in re.findall("(\d+) (\w+)", content):
        d[c] = max(d[c], int(n))

    if all(d[c] <= n for c, n in allowed.items()):
        part1 += idx
    part2 += math.prod(d.values())

print(part1)
print(part2)
