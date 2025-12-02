from collections import defaultdict
import itertools
import numpy as np

with open("08.in") as f:
    lines = [line.strip() for line in f.readlines()]

lines = np.array([[*line] for line in lines])
rows, cols = lines.shape

d = defaultdict(list)
for r, c in zip(*np.where(lines != '.')):
    d[lines[r, c]].append((r, c))

anti = set()
anti2 = set()

def bcheck(r,c):
    return 0 <= r < rows and 0 <= c < cols

for k, v in d.items():
    for (r1,c1),(r2,c2) in itertools.combinations(v, 2):
        dr = r1-r2
        dc = c1-c2
        if bcheck(r1+dr, c1+dc):
            anti.add((r1+dr, c1+dc))
        if bcheck(r2-dr, c2-dc):
            anti.add((r2-dr, c2-dc))

        for x in itertools.count():
            r = r1 + x * dr
            c = c1 + x * dc
            if not bcheck(r,c):
                break
            anti2.add((r,c))

        for x in itertools.count():
            r = r1 - x * dr
            c = c1 - x * dc
            if not bcheck(r,c):
                break
            anti2.add((r,c))
print(len(anti))
print(len(anti2))
