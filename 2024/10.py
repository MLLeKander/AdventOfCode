import numpy as np
with open("10.in") as f:
    lines = [line.strip() for line in f.readlines()]

lines = np.array([[-1 if x == '.' else int(x) for x in line] for line in lines])
rows, cols = lines.shape
paths = [[set() for _ in range(cols)] for _ in range(rows)]
cnts = np.zeros(lines.shape, dtype=int)

for x in range(10):
    for r in range(rows):
        for c in range(cols):
            if lines[r,c] == x:
                if x == 0:
                    cnts[r][c] = 1
                    paths[r][c] = {(r,c)}
                else:
                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                        if 0 <= r+dr < rows and 0 <= c+dc < cols:
                            if lines[r+dr, c+dc] == x-1:
                                paths[r][c] |= paths[r+dr][c+dc]
                                cnts[r][c] += cnts[r+dr][c+dc]

out1 = 0
out2 = 0
for r in range(rows):
    for c in range(cols):
        if lines[r][c] == 9:
            out1 += len(paths[r][c])
            out2 += cnts[r][c]
print(out1)
print(out2)
