from collections import defaultdict

with open("23.in") as f:
    lines = [line.strip() for line in f.readlines()]

adj = defaultdict(set)

for line in lines:
    a, b = line.split("-")
    adj[a].add(b)
    adj[b].add(a)

visited = set()
#res = set()
out = 0
for tmp, tmp_adj in adj.items():
    if tmp[0] != "t":
        continue
    visited.add(tmp)
    for tmp2, tmp2_adj in adj.items():
        if tmp2 not in tmp_adj or tmp2 in visited:
            continue
        for tmp3 in tmp_adj & tmp2_adj:
            if tmp3 in visited:
                continue
            #res.add(tuple(sorted([tmp,tmp2,tmp3])))
            out += 1
print(out//2)

import networkx as nx
G=nx.Graph()
for x1, lst in adj.items():
    for x2 in lst:
        G.add_edge(x1, x2)
cl = nx.approximation.max_clique(G)
print(','.join(sorted(cl)))
