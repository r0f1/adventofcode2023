from pathlib import Path

lines = Path("input.txt").read_text().splitlines()
seeds = list(map(int, lines[0].split(": ")[1].split()))
maps = []
for line in lines[2:]:
    if line.endswith(":"):
        map = {}
        maps.append(map)
    elif len(line) > 0:
        dest, source, n = [int(i) for i in line.split()]
        map[source] = (dest, n)
    
maps_clean = [dict(sorted(map.items())) for map in maps]

loc = float("inf")
for seed in seeds:
    k = seed
    for map in maps_clean:
        for s, (d, n) in map.items():
            if s <= k < s+n:
                k += d - s
                break
    loc = min(k, loc)
print(loc)
