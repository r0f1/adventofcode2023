from itertools import pairwise
from itertools import product
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

start_y, start_x = 0, 0

for row, l in enumerate(lines):
    pos = l.find("S")
    if pos >= 0:
        start_y = row
        start_x = pos
        break

max_y = len(lines)
max_x = len(lines[0])
nodes = {(r, c): 0 for r, c in product(range(max_y), range(max_x))}

seen = set()
explore = [(start_y, start_x)]
path = []

while explore:
    y, x = explore.pop(0)
    if (y, x) in seen:
        continue

    path.append((y,x))

    c = lines[y][x]
    d = nodes[(y, x)] + 1
    seen.add((y, x))

    north = ("|", "7", "F")
    east = ("-", "J", "7")
    south = ("|", "L", "J")
    west = ("-", "L", "F")

    if y > 0 and lines[y-1][x] in north and (c in south or c == "S"):
        v = (y-1, x)
        if v not in seen:
            nodes[v] = d
            explore.append(v)

    if x < max_x-1 and lines[y][x+1] in east and (c in west or c == "S"):
        v = (y, x+1)
        if v not in seen:
            nodes[v] = d
            explore.append(v)

    if y < max_y-1 and lines[y+1][x] in south and (c in north or c == "S"):
        v = (y+1, x)
        if v not in seen:
            nodes[v] = d
            explore.append(v)

    if x > 0 and lines[y][x-1] in west and (c in east or c == "S"):
        v = (y, x-1)
        if v not in seen:
            nodes[v] = d
            explore.append(v)

path = path[::2] + path[1::2]
l = len(path) // 2
path = path[:l] + list(reversed(path[l:]))

print(max(nodes.values()))

# https://en.wikipedia.org/wiki/Shoelace_formula
sum = 0
for i in range(len(path)):
    y1, x1 = path[i]
    y2, x2 = path[(i+1)%len(path)]
    sum += x1 * y2 - y1 * x2
area = abs(sum/2)

# https://en.wikipedia.org/wiki/Pick%27s_theorem
print(area-len(path)/2+1)

