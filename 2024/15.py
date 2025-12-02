with open("15.in") as f:
    lines = [line.strip() for line in f.readlines()]

midp = lines.index("")
board = [[*line] for line in lines[:midp]]
instructions = "".join(lines[midp+1:])


for start_r in range(len(board)):
    if "@" in board[start_r]:
        start_c = board[start_r].index("@")
        break

robot_r, robot_c = start_r, start_c

for instruction in instructions:
    dr = dc = 0
    if instruction == "<":
        dc = -1
    elif instruction == ">":
        dc = 1
    elif instruction == "^":
        dr = -1
    elif instruction == "v":
        dr = 1

    target_r = robot_r + dr
    target_c = robot_c + dc

    while board[target_r][target_c] == "O":
        target_r += dr
        target_c += dc
    
    if board[target_r][target_c] == ".":
        board[target_r][target_c] = "O"
        board[robot_r][robot_c] = "."
        robot_r += dr
        robot_c += dc
        board[robot_r][robot_c] = "@"

out = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "O":
            out += 100 * r + c
print(out)

def remap(line):
    return [*"".join(line).replace(".", "..").replace("#", "##").replace("O", "[]").replace("@", "@.")]
board = [[*line] for line in lines[:midp]]
board = [remap(line) for line in board]
robot_r, robot_c = start_r, start_c*2

def can_move_vert(r, c, dr):
    n = board[r][c]
    if n == ".":
        return True
    if n == "@":
        return can_move_vert(r+dr, c, dr)
    if n == "[":
        return can_move_vert(r+dr, c, dr) and can_move_vert(r+dr, c+1, dr)
    if n == "]":
        return can_move_vert(r+dr, c, dr) and can_move_vert(r+dr, c-1, dr)
    if n == "#":
        return False
def move_vert(r, c, dr):
    n = board[r][c]
    n2 = board[r+dr][c]
    if n2 == "[":
        move_vert(r+dr, c, dr)
        move_vert(r+dr, c+1, dr)
    if n2 == "]":
        move_vert(r+dr, c, dr)
        move_vert(r+dr, c-1, dr)
    board[r+dr][c] = board[r][c]
    board[r][c] = "."


for instruction in instructions:
    dr = dc = 0
    if instruction == "<":
        dc = -1
    elif instruction == ">":
        dc = 1
    elif instruction == "^":
        dr = -1
    elif instruction == "v":
        dr = 1

    if dc == 0:
        if can_move_vert(robot_r, robot_c, dr):
            move_vert(robot_r, robot_c, dr)
            robot_r += dr
    else:
        tmp_c = robot_c
        while board[robot_r][tmp_c] not in ".#":
            tmp_c += dc
        if board[robot_r][tmp_c] == ".":
            while tmp_c != robot_c:
                board[robot_r][tmp_c] = board[robot_r][tmp_c-dc]
                tmp_c -= dc
            board[robot_r][robot_c] = "."
            robot_c += dc

out = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "[":
            out += 100 * r + c
print(out)
