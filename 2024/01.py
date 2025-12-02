l1, l2 = [], []
for line in open("01.in").readlines():
    a, b = line.strip().split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()
print(sum(abs(a-b) for a, b in zip(l1, l2)))

from collections import Counter
c = Counter(l2)
print(sum(x * c.get(x,0) for x in l1))
