from collections import Counter

with open("22.in") as f:
    lines = [line.strip() for line in f.readlines()]

MOD = 16777216

def step(x):
    x ^= x * 64
    x %= MOD
    x ^= x // 32
    x %= MOD
    x ^= x * 2048
    x %= MOD
    return x

out = 0
cnt = Counter()
for line in lines:
    x = int(line)
    diffs = []
    seen_deltas = set()
    for _ in range(2000):
        prev = x
        x = step(x)
        diffs.append(((prev%10) - (x%10), x%10))
    for ndx in range(len(diffs)-4):
        curr = diffs[ndx:ndx+4]
        delta = tuple(x[0] for x in curr)
        if len(delta) != 4:
            print("???")
        if delta in seen_deltas:
            continue
        seen_deltas.add(delta)
        cnt[delta] += curr[-1][1]
    out += x
print(out)
print(max(cnt.values()))
