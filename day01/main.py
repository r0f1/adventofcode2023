with open("input.txt") as f:
    lines = [x.strip() for x in f]

# Part 1
digits = [[d for d in l if d.isdigit()] for l in lines]
values = [int(d[0]+d[-1]) for d in digits]
print(sum(values))

# Part 2
# difficulty: number strings can be overlapping --> using string replacement
patterns = [("one", "o1e"), ("two", "t2o"), ("three", "t3e"),
            ("four", "f4r"), ("five", "f5e"), ("six", "s6x"),
            ("seven", "s7n"), ("eight", "e8t"), ("nine", "n9e")]
values = []
for l in lines:
    for p in patterns:
        l = l.replace(*p)
    ds = [d for d in l if d.isdigit()]
    values.append(int(ds[0]+ds[-1]))
print(sum(values))
