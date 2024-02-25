from pathlib import Path
import re
import numpy as np
from skimage.measure import label
from collections import defaultdict

lines = Path("input.txt").read_text().splitlines()
grid = []
for l in lines:
    s = re.sub(r"\d", ".", l)
    s = s.replace(".", "0")
    s = re.sub(r"\*", "2", s)
    s = re.sub(r"\W", "1", s)
    grid.append(list(s))
grid = np.array(grid).astype("uint8")
grid2 = label((grid > 1).astype("uint8"))

max_y, max_x = grid.shape
gears = defaultdict(list)

res = 0
for y, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        x1, x2 = m.start(), m.end()
        coords = [(x1-1, y), (x2, y)]
        for i in range(x1-1, x2+1):
            coords.append((i, y-1))
            coords.append((i, y+1))
        coords = [(cx, cy) for cx, cy in coords if cx > 0 and cx < max_x and cy > 0 and cy < max_y]
        for cx, cy in coords:
            if grid[cy][cx] > 0:
                n = int(m.group(0))
                res += n
                if grid2[cy][cx] > 0:
                    gears[grid2[cy][cx]].append(n)
                break
print(res)
print(sum([np.prod(v) for v in gears.values() if len(v) > 1]))
