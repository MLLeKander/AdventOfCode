with open("04.in") as f:
    lines = [list(l.strip()) for l in f.readlines()]

R = len(lines)
C = len(lines[0])

def iteration():
    out = 0

    marks = []
    for r in range(R):
        for c in range(C):
            if lines[r][c] == "@":
                count = 0
                for nr in range(max(0,r-1),min(R,r+2)):
                    for nc in range(max(0,c-1),min(C,c+2)):
                        if (nr != r or nc != c):
                            count += lines[nr][nc] == "@"
                if count < 4:
                    marks.append((r,c))
                    out += 1

    for r,c in marks:
        lines[r][c] = "."

    return out

ans2 = ans1 = iteration()
while (tmp := iteration()) != 0:
    ans2 += tmp
print(ans1, ans2)
