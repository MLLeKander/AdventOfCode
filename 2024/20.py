from collections import Counter, deque

with open("20.in") as f:
    lines = [line.strip() for line in f.readlines()]

start = end = None
rows = len(lines)
cols = len(lines[0])

for row in range(rows):
    for col in range(cols):
        if lines[row][col] == "S":
            start = (row,col)
        elif lines[row][col] == "E":
            end = (row,col)

q = deque([(0,end)])
mindist = {}
while len(q) > 0:
    dist, (row, col) = q.popleft()

    if (row,col) in mindist:
        continue

    mindist[(row,col)] = dist

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        if 0 <= row+dr < rows and 0 <= col+dc < cols and lines[row+dr][col+dc] != "#":
            q.append((dist+1, (row+dr, col+dc)))


def make_deltas(max_len):
    out = []
    for i in range(-max_len,max_len+1):
        space = max_len-abs(i)
        for j in range(-space, space+1):
            out.append((i,j))
    return out

cheats = Counter()
deltas = make_deltas(2)
for row in range(rows):
    for col in range(cols):
        if (row,col) not in mindist:
            continue
        currdist = mindist[(row,col)]
        for dr, dc in make_deltas(2):
            if (row+dr,col+dc) in mindist and lines[row+dr][col+dc] != "#" and mindist[(row+dr,col+dc)] < currdist - 2:
                cheats[currdist - 2 - mindist[(row+dr,col+dc)]] += 1

out = 0
for k,v in cheats.items():
    if k >= 100:
        out += v
print(out)

cheats = Counter()
for row in range(rows):
    for col in range(cols):
        if (row,col) not in mindist:
            continue
        currdist = mindist[(row,col)]
        for dr, dc in make_deltas(20):
            if (row+dr,col+dc) in mindist and lines[row+dr][col+dc] != "#" and mindist[(row+dr,col+dc)] < currdist - abs(dr) - abs(dc):
                cheats[currdist - abs(dr) - abs(dc) - mindist[(row+dr,col+dc)]] += 1

out = 0
for k,v in cheats.items():
    if k >= 100:
        out += v
print(out)
