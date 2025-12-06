with open("05.in") as f:
    lines = [l.strip() for l in f.readlines()]

ranges = []
liter = iter(lines)
while "-" in (line := next(liter)):
    lo, hi = [int(x) for x in line.split("-")]
    ranges.append(range(lo, hi+1))
ranges.sort(key=lambda x: (x.start, x.stop))

ans1 = 0
for line in liter:
    i = int(line)
    ans1 += any(i in r for r in ranges)


ans2 = 0
lcursor = rcursor = -1

for r in ranges:
    if r.start > lcursor:
        ans2 += lcursor - rcursor
        rcursor = r.start
        lcursor = r.stop
    elif r.stop > lcursor:
        lcursor = r.stop
ans2 += lcursor - rcursor

print(ans1, ans2)
