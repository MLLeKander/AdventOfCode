import numpy as np

with open("06.in") as f:
    lines = [line.strip() for line in f.readlines()]


rows = len(lines)
cols = len(lines[0])
row = [ndx for ndx, s in enumerate(lines) if "^" in s][0]
col = lines[row].index("^")

lines = np.array([[*x] for x in lines])

visited = set()
visited_dir = set()
obstructions = set()
dr = -1
dc = 0

turnmap = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0),
}
charmap = {
    (-1,0): "^",
    (0,1): ">",
    (1,0): "V",
    (0,-1): "<",
}

def bound_check(r,c):
    return 0 <= r < rows and 0 <= c < cols

def check_turn(r, c, dr, dc):
    dr, dc = turnmap[(dr,dc)]

    while True:
        if lines[r][c] == "#":
            return False
        if lines[r][c] == "&":
            return True

        r += dr
        c += dc
        if not bound_check(r, c):
            break
    return False

def p():
    print("\n".join("".join(x for x in line) for line in lines))

while True:
    visited.add((row, col))
    lines[row][col] = charmap[(dr,dc)]

    if bound_check(row+dr, col+dc) and lines[row+dr][col+dc] == "." and check_turn(row, col, dr, dc):
        obstructions.add((row+dr, col+dc))
        lines[row+dr][col+dc] = "*"

    row += dr
    col += dc

    if not bound_check(row, col):
        break

    if lines[row][col] in ("#", "&"):
        lines[row][col] = "&"
        row -= dr
        col -= dc

        dr, dc = turnmap[(dr,dc)]

        row += dr
        col += dc


print(len(visited))
print(len(obstructions))
