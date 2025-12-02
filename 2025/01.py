with open("01.in") as f:
    lines = [l.strip() for l in f.readlines()]

pos = 50
ans2 = ans1 = 0
for line in lines:
    for _ in range(int(line[1:])):
        pos += -1 if line[0] == "L" else 1
        pos %= 100
        if pos == 0:
            ans2 += 1
    if pos == 0:
        ans1 += 1
print(ans1, ans2)
