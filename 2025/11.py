from collections import defaultdict

with open("11.in") as f:
   lines = [l for l in f.readlines()]

out_edges = defaultdict(list)
in_edges = defaultdict(list)
for line in lines:
    a, *b = line.split()
    a = a[:-1]

    out_edges[a] = b
    for x in b:
        in_edges[x].append(a)
nodes = out_edges.keys() | in_edges.keys()

def count_paths(start, target):
    visit_count = defaultdict(int)
    paths_count = defaultdict(int)

    q = []
    for node in nodes:
        if len(in_edges[node]) == 0:
            q.append(node)

    paths_count[start] = 1

    while len(q) > 0:
        curr = q.pop()
        if curr == target:
            return paths_count[target]

        for adj in out_edges[curr]:
            paths_count[adj] += paths_count[curr]
            visit_count[adj] += 1
            if visit_count[adj] == len(in_edges[adj]):
                q.append(adj)

    return 0

print(count_paths("you", "out"))

mid_paths = count_paths("fft", "dac")
if mid_paths != 0:
    a, b = "fft", "dac"
else:
    mid_paths = count_paths("dac", "fft")
    a, b = "dac", "fft"

print(count_paths("svr", a) * mid_paths * count_paths(b, "out"))
