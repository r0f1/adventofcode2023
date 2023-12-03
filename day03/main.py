import numpy as np
import re
from skimage.morphology import dilation
from skimage.morphology import square

with open("test.txt") as f:
    lines = [x.strip() for x in f]

syms = []
for l in lines:
    l = re.sub(r"\d", ".", l)
    l = l.replace(".", "0")
    l = re.sub("\W", "1", l)
    syms.append(l)

valid = np.array([list(s) for s in syms]).astype("uint8")
valid = dilation(valid, square(3))
print(valid)

for l in lines:
    re.findall("\d+", l)