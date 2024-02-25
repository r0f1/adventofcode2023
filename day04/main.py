from pathlib import Path
from collections import defaultdict

lines = Path("input.txt").read_text().splitlines()

res = 0
cards = {(i+1): 1 for i in range(len(lines))}

for i, line in enumerate(lines, start=1):
    a, b = line.split(" | ")
    a = a.split(": ")[1]
    a, b = set(a.split()), set(b.split())

    m = len(a & b)
    if m > 0:
        res += 2 ** (m-1)

    for k in range(i+1, i+m+1):
        cards[k] += cards[i]
        
print(res)
print(sum(cards.values()))
