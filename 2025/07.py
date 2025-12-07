from collections import defaultdict

with open("07.in") as f:
    lines = [list(l) for l in f.readlines()]

positions = {lines[0].index("S"): 1}
ans1 = 0
for line in lines[1:]:
    next_positions = defaultdict(int)
    for position, cnt in positions.items():
        if line[position] == "^":
            ans1 += 1
            next_positions[position-1] += cnt
            next_positions[position+1] += cnt
        else:
            next_positions[position] += cnt
    positions = next_positions
ans2 = sum(positions.values())
print(ans1, ans2)
