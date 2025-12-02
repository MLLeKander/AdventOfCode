from collections import defaultdict, Counter
import networkx as nx
with open("24.fixed.in") as f:
    lines = [line.strip() for line in f.readlines()]

wires = {}
ops = []
for line in lines:
    if len(line.split()) == 2:
        wire, val = line.split()
        wires[wire[:-1]] = val == "1"
    elif line != "":
        ops.append(line.split())

base_ops = ops
while len(ops) > 0:
    ops2 = []
    for x in ops:
        w1, op, w2, _, w3 = x
        if w1 not in wires or w2 not in wires:
            ops2.append(x)
        else:
            if op == "OR":
                wires[w3] = wires[w1] | wires[w2]
            elif op == "AND":
                wires[w3] = wires[w1] & wires[w2]
            elif op == "XOR":
                wires[w3] = wires[w1] ^ wires[w2]
            else:
                print("????")
    ops = ops2

zs = sorted([(k,v) for k,v in wires.items() if k.startswith("z")], reverse=True)
print(int(''.join("1" if v else "0" for k,v in zs), 2))

adj = defaultdict(list)
radj = defaultdict(list)
nodes = set()
G = nx.DiGraph()

op_to_color = {
    "AND": "pink",
    "OR": "lightgreen",
    "XOR": "lightblue",
}
colors = {}
ops = {}
for w1, op, w2, _, w3 in base_ops:
    adj[w1].append(w3)
    adj[w2].append(w3)
    radj[w3].append(w1)
    radj[w3].append(w2)
    G.add_edge(w1,w3)
    G.add_edge(w2,w3)
    nodes.add(w1)
    nodes.add(w2)
    nodes.add(w3)

    colors[w3] = op_to_color[op]
    ops[w3] = op

q = [n for n in nodes if n.startswith(("x","y"))]
val = defaultdict(int)
for n in q:
    colors[n] = "yellow"

cnt = Counter()
while len(q) > 0:
    curr = q.pop()
    for tmp in adj[curr]:
        val[tmp] = max(val[tmp], val[curr]+1)
        cnt[tmp] += 1
        if cnt[tmp] == 2:
            q.append(tmp)

pos = {}
for n in sorted(nodes, key=lambda x: val[x]):
    if val[n] == 0:
        if n.startswith("x"):
            pos[n] = (0, 10*float(n[1:]))
        if n.startswith("y"):
            pos[n] = (0, 10*float(n[1:])+5)
    else:
        a,b = radj[n]
        op = ops[n]
        offset = 2 if op == "AND" else -2 if op == "OR" else 0
        pos[n] = (val[n], offset + (pos[a][1] + pos[b][1])/2)
maxcol = max(x for x,y in pos.values())
for n in nodes:
    if n.startswith("z"):
        pos[n] = (maxcol+1, 10*float(n[1:]))
        

import matplotlib.pyplot as plt
nx.draw_networkx(G, pos, node_color=[colors[n] for n in G.nodes()])
plt.show()

print(",".join(sorted(["qjj","cbj","cfk","z35","z18","dmn","z07","gmt"])))
"""
z35,cfk
z18,dmn
dnt,mhf
z07,gmt
"""
