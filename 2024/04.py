with open("04.txt") as f:
    lines = [line.strip() for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])
def search(row, col, dr, dc):
    last_row = row+3*dr
    last_col = col+3*dc
    if last_row < 0 or last_row >= rows or last_col < 0 or last_col >= cols:
        return False

    for x in range(4):
        r = row+x*dr
        c = col+x*dc
        if lines[r][c] != "XMAS"[x]:
            return False
    return True

out = 0
for row in range(rows):
    for col in range(cols):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            if search(row, col, dr, dc):
                out += 1
print(out)

def search2(row, col):
    if lines[row][col] != "A" or row < 1 or row >= rows-1 or col < 1 or col >= cols-1:
        return False
    a = [lines[row-1][col-1], lines[row+1][col+1]]
    b = [lines[row+1][col-1], lines[row-1][col+1]]
    return sorted(a) == [*"MS"] and sorted(b) == [*"MS"]

out = 0
for row in range(rows):
    for col in range(cols):
        if search2(row, col):
            out += 1
print(out)
