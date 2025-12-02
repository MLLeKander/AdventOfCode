from collections import defaultdict

with open("05.in") as f:
    lines = [line.strip() for line in f.readlines()]

it = iter(lines)

rules = set()
while True:
    line = next(it)
    if line == "":
        break

    a, b = line.split("|")
    rules.add((a,b))

lines = []
try:
    while True:
        lines.append(next(it).split(","))
except:
    pass

def is_sorted(line):
    for a, b in zip(line, line[1:]):
        if (a,b) not in rules:
            return 0
    return int(line[len(line)//2])

def toposort(line):
    adj = defaultdict(list)
    for a in line:
        for b in line:
            if (a,b) in rules:
                adj[a].append(b)

    q = []
    for x in line:
        if x not in adj:
            q.append(x)

    out = []
    while len(q) > 0:
        x = q.pop()
        out.append(x)
        for k, v in list(adj.items()):
            if x in v:
                v.remove(x)
                if len(v) == 0:
                    adj.pop(k)
                    q.append(k)
    res = is_sorted(out[::-1])
    if res == 0:
        print("???")
    return res

out = 0
out_unsorted = 0
for line in lines:
    a_result = is_sorted(line)
    if a_result:
        out += is_sorted(line)
    else:
        out_unsorted += toposort(line)

print(out)
print(out_unsorted)
