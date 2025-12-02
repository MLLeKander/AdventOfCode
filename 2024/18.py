import collections

with open("18.in") as f:
    lines = [line.strip() for line in f.readlines()]

height, width = 70, 70

def find_path_length(timestep):
    board = [["."] * (width+1) for _ in range(height+1)]

    for line in lines[:timestep]:
        c,r = [int(x) for x in line.split(",")]
        board[r][c] = "#"

    visited = set()
    dq = collections.deque([((0,0),0)])
    while len(dq) > 0:
        curr, cnt = dq.popleft()

        r,c = curr
        if r == height and c == width:
            return cnt
            break

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_state = (r+dr, c+dc)
            if 0 <= r+dr <= height and 0 <= c+dc <= width and next_state not in visited and board[r+dr][c+dc] != "#":
                
                visited.add(next_state)
                dq.append((next_state, cnt+1))

    return -1

print(find_path_length(1024))

lo = 1025
hi = len(lines)-1

"""
import tqdm
for ts in tqdm.tqdm(range(lo, hi)):
    if find_path_length(ts) < 0:
        break
print(ts)
"""
while lo < hi:
    mid = (lo + hi) // 2
    if find_path_length(mid) > 0:
        lo = mid+1
    else:
        hi = mid
print(lo, hi, mid)
print(lines[lo-1])
