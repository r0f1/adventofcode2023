from pathlib import Path

lines = Path("input.txt").read_text().splitlines()
seeds = list(map(int, lines[0].split(": ")[1].split()))
maps = []
for line in lines[2:]:
    if line.endswith(":"):
        map = []
        maps.append(map)
    elif len(line) > 0:
        map.append([int(i) for i in line.split()])
    
loc = float("inf")
for seed in seeds:
    k = seed
    for map in maps:
        for d, s, n in map:
            if s <= k < s+n:
                k += d - s
                break
    loc = min(k, loc)
print(loc)

def treat_intervals(map, items):
    res = []
    for d, s, n in map:
      new_items = []
      while items:
        a, b = items.pop()
        before = (a, min(b,s))
        inter = (max(a, s), min(s+n, b))
        after = (max(s+n, a), b)
        
        if before[1]>before[0]:
          new_items.append(before)
        if inter[1]>inter[0]:
          res.append((inter[0]-s+d, inter[1]-s+d))
        if after[1]>after[0]:
          new_items.append(after)
      items = new_items
    return res + items

loc = float("inf")
for seed_start, seed_len in zip(seeds[::2], seeds[1::2]):
    k = [(seed_start, seed_start+seed_len)]
    for map in maps:
        k = treat_intervals(map, k)
    loc = min(min(k)[0], loc)
print(loc)
