from collections import Counter
from functools import cmp_to_key
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()
hands = [(a, int(b)) for a, b in [l.split() for l in lines]]

def compare_image(a, b):
    a = sorted(Counter(a).values(), reverse=True)
    b = sorted(Counter(b).values(), reverse=True)
    for ca, cb in zip(a, b):
        if ca == cb:
            if ca in (2,3): continue
            else: break
        if ca > cb: return 1
        else: return -1
    return 0

def compare_numbers(a, b, n):
    for ia, ib in zip(a, b):
        if ia == ib: continue
        return n.find(ia) - n.find(ib)

def compare_part1(a, b):
    a, b = a[0], b[0]
    res = compare_image(a, b)
    if res == 0:
        return compare_numbers(a, b, "23456789TJQKA")
    return res

def compare_part2(a, b):
    a, ima = a[:2]
    b, imb = b[:2]
    res = compare_image(ima, imb)
    if res == 0:
        return compare_numbers(a, b, "J23456789TQKA")
    return res

def compare_symbol(a, b):
    if a[1] == b[1]:
        n = "23456789TJQKA"
        return n.find(b[0]) - n.find(a[0])
    return b[1] - a[1]

def convert(items):
    res = []
    for a, b in items:
        if not "J" in a:
            im = a
        elif a == "JJJJJ":
            im = "AAAAA"
        else:
            counts = Counter(a)
            counts.pop("J")
            c = sorted(counts.items(), key=cmp_to_key(compare_symbol))[0][0]
            im = a.replace("J", c)
        res.append((a, im, b))
    return res

s = sorted(hands, key=cmp_to_key(compare_part1))
print(sum(i*b for i, (_, b) in enumerate(s, start=1)))

s = sorted(convert(hands), key=cmp_to_key(compare_part2))
print(sum(i*b for i, (_, _, b) in enumerate(s, start=1)))

