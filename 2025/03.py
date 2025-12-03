with open("03.in") as f:
    lines = [l.strip() for l in f.readlines()]

ans2 = ans1 = 0
for line in lines:
    batteries = [int(x) for x in line]

    b1 = max(batteries[:-1])
    b2 = max(batteries[batteries.index(b1)+1:])
    ans1 += 10*b1 + b2

    cursor = 0
    res = 0
    for ndx in range(12):
        curr = max(batteries[cursor:len(batteries)+ndx-11])
        cursor += batteries[cursor:].index(curr)+1
        res = 10 * res + curr
    ans2 += res

print(ans1, ans2)
