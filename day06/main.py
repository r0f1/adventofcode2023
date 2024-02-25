from math import prod

# values = [(47, 207), (84, 1394), (74, 1209), (67, 1014)]
values = [(47847467, 207139412091014)]

print(prod(sum(i * (t-i) > r for i in range(t)) for t, r in values))
