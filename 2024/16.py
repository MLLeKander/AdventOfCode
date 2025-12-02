from heapq import heappush, heappop

with open("16.in") as f:
    lines = [line.strip() for line in f.readlines()]

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "S":
            start = (r,c)
        if lines[r][c] == "E":
            target = (r,c)

q = [(0, *start, 0, 1)]
visited = set()

prevs = {}

out = None
while True:
    state = heappop(q)
    if state[1:] in visited:
        continue
    visited.add(state[1:])

    score, r, c, dr, dc = state
    if out is not None and score > out:
        break

    if lines[r][c] == "E":
        out = score
        continue

    def add(next_score, next_r, next_c, next_dr, next_dc):
        next_state = (next_r, next_c, next_dr, next_dc)
        curr_state = (r, c, dr, dc)
        if next_state in prevs:
            if prevs[next_state][0] == next_score:
                prevs[next_state][1].append(curr_state)
            elif prevs[next_state][0] > next_score:
                prevs[next_state] = (next_score, [curr_state])
        else:
            prevs[next_state] = (next_score, [curr_state])

        heappush(q, (next_score, next_r, next_c, next_dr, next_dc))

    if lines[r+dr][c+dc] != "#":
        add(score+1, r+dr, c+dc, dr, dc)

    if dr == 0:
        add(score+1000, r, c, -1, 0)
        add(score+1000, r, c, 1, 0)
    else:
        add(score+1000, r, c, 0, -1)
        add(score+1000, r, c, 0, 1)

print(out)

out = 0
visited = set()
good_seats = set()
q = [(*target, *d) for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]] 
while len(q) > 0:
    state = q.pop()
    if state in visited:
        continue
    visited.add(state)
    good_seats.add(state[:2])
    if state in prevs:
        q.extend(prevs[state][1])

print(len(good_seats))
