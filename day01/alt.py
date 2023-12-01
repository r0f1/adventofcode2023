import regex as re

with open("input.txt") as f:
    lines = [x.strip() for x in f]

# Part 2
words = "one,two,three,four,five,six,seven,eight,nine".split(",")
pattern = "[0-9]|" + "|".join(words)
d = dict((f"{i}", i) for i in range(10)) | dict((e, i) for i, e in enumerate(words, start=1))

values = []
for l in lines:
    ms = re.findall(pattern, l, overlapped=True)
    a, b = d[ms[0]], d[ms[-1]]
    values.append(10*a+b)

print(sum(values))
