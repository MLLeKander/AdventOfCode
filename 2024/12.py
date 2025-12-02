import numpy as np

with open("12.in") as f:
    lines = [line.strip() for line in f.readlines()]

lines = np.array([[*line] for line in lines])
rows, cols = lines.shape

def process_region(start_r, start_c):
    plant = lines[start_r][start_c]

    fences = np.zeros((rows*2+1, cols*2+1), dtype=int)
    queue = [(start_r, start_c)]
    visited = set(queue)
    perim = 0

    while len(queue) > 0:
        curr_r, curr_c = queue.pop()

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_r = curr_r + dr
            next_c = curr_c + dc

            if (next_r, next_c) in visited:
                continue
            if 0 <= next_r < rows and 0 <= next_c < cols and lines[next_r][next_c] == plant:
                visited.add((next_r, next_c))
                queue.append((next_r, next_c))
            else:
                fences[curr_r*2+dr+1][curr_c*2+dc+1] = dr*2 + dc
                perim += 1

    for r,c in visited:
        lines[r][c] = '.'


    sides = 0
    for r in range(fences.shape[0]):
        for c in range(fences.shape[1]):
            fence = fences[r][c]
            if fence == 0:
                continue
            dr = dc = 0
            if abs(fence) == 1:
                dr = 2
            else:
                dc = 2

            curr_r = r
            curr_c = c
            while curr_r < fences.shape[0] and curr_c < fences.shape[1]:
                if fences[curr_r][curr_c] != fence:
                    break
                fences[curr_r][curr_c] = 0
                curr_r += dr
                curr_c += dc

            sides += 1
            #print(r, c, dr,dc)
            #print(fences)

    return len(visited), perim, sides

out1 = 0
out2 = 0
for r in range(rows):
    for c in range(cols):
        if lines[r][c] != '.':
            area, perim, sides = process_region(r, c)
            out1 += area * perim
            out2 += area * sides
print(out1)
print(out2)
