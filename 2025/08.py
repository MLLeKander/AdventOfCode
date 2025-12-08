from collections import Counter
import math

with open("08.in") as f:
    lines = [l for l in f.readlines()]

boxes = [list(map(int, line.split(","))) for line in lines]

def get_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

dists = []
for andx, a in enumerate(boxes):
    for bndx, b in enumerate(boxes[andx+1:], andx+1):
        dists.append((get_dist(a,b), andx, bndx))
dists.sort()

class DisjointSet:
    def __init__(self, items):
        self.parents = {item: item for item in items}

    def find_root(self, item):
        if self.parents[item] != item:
            self.parents[item] = self.find_root(self.parents[item])
        return self.parents[item]

    def union(self, itemA, itemB):
        rootA = self.find_root(itemA)
        rootB = self.find_root(itemB)

        if rootA == rootB:
            return False

        self.parents[rootA] = rootB
        return True

dj = DisjointSet(range(len(boxes)))
union_count = 0
for dist, andx, bndx in dists[:1000]:
    union_count += 1 if dj.union(andx, bndx) else 0

cnt = Counter(dj.find_root(x) for x in range(len(boxes)))

print(math.prod(x[1] for x in cnt.most_common(3)))


dj = DisjointSet(range(len(boxes)))
for dist, andx, bndx in dists:
    if dj.union(andx, bndx):
        res = andx, bndx
print(boxes[res[0]][0]*boxes[res[1]][0])
