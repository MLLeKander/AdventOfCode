from collections import Counter
with open("11.in") as f:
    lines = [line.strip() for line in f.readlines()]
inp = Counter([int(x) for x in lines[0].split()])

def blink(inp):
    next_inp = Counter()
    for stone, cnt in inp.items():
        s = str(stone)
        if stone == 0:
            next_inp[1] += cnt
        elif len(s) % 2 == 0:
            midp = len(s)//2
            next_inp[int(s[:midp])] += cnt
            next_inp[int(s[midp:])] += cnt
        else:
            next_inp[stone * 2024] += cnt
    return next_inp
for _ in range(25):
    inp = blink(inp)
print(sum(inp.values()))

for _ in range(50):
    inp = blink(inp)
print(sum(inp.values()))
