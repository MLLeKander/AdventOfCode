import re

with open("14.in") as f:
    lines = [line.strip() for line in f.readlines()]

robots = [re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups() for line in lines]
robots = [[int(x) for x in robot] for robot in robots]

width, height = 101, 103

q1 = q2 = q3 = q4 = 0

for c,r,dc,dr in robots:
    c = (c + dc * 100) % width
    r = (r + dr * 100) % height
    if c < 50:
        if r < 51:
            q1 += 1
        elif r > 51:
            q2 += 1
    elif c > 50:
        if r < 51:
            q3 += 1
        elif r > 51:
            q4 += 1

print(q1*q2*q3*q4)

for t in range(height*width):
    board = [[" "] * width for _ in range(height)]
    for c,r,dc,dr in robots:
        c = (c + dc * t) % width
        r = (r + dr * t) % height
        board[r][c] = "*"
    print("="*width)
    print(t)
    print("\n".join("".join(x for x in line) for line in board))
