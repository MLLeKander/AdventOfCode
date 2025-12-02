import numpy as np
with open("25.in") as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")

locks = []
keys = []
for *x, _ in zip(*[lines[i::8] for i in range(8)]):
    is_lock = all(c == "#" for c in x[0])
    tmp = [list(line).count("#")-1 for line in np.array([[*line] for line in x]).T]
    print(tmp, is_lock)
    (locks if is_lock else keys).append(tmp)

def is_compatible(lock, key):
    for x,y in zip(lock, key):
        if x+y > 5:
            return False
    return True

print(len(keys), len(locks))
out = 0
for lock in locks:
    for key in keys:
        if is_compatible(lock, key):
            out += 1
print(out)
