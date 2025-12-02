import re

with open("02.in") as f:
    lines = [line.strip() for line in f.readlines()]

out1 = 0
out2 = 0
for line in lines:
    game, s = re.match(r"Game (\d+): (.*)", line).groups()

    counts = {"red": 0, "blue": 0, "green": 0}
    for round in s.split("; "):
        for x in round.split(", "):
            cnt, color = x.split(" ")
            counts[color] = max(counts[color], int(cnt))
    if counts["red"] <= 12 or counts["green"] <= 13 or counts["blue"] <= 14:
        out1 += int(game)
    out2 += counts["red"] * counts["green"] * counts["blue"]
print(out1)
print(out2)
