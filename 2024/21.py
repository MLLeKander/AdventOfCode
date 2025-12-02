from collections import Counter

with open("21.in") as f:
    lines = [line.strip() for line in f.readlines()]

nums = "789\n456\n123\n 0A".split("\n")
dirs = " ^A\n<v>".split("\n")

def expand(target, pad):
    pad_map = {(rndx,cndx):c for rndx, row in enumerate(pad) for cndx, c in enumerate(row) if c != ' '}
    inv_pad_map = {c:pos for pos, c in pad_map.items()}

    curr_r, curr_c = inv_pad_map["A"]
    out = ""
    for ch in target:
        target_r, target_c = inv_pad_map[ch]
        dr = target_r - curr_r
        dc = target_c - curr_c

        v = "v"*dr if dr > 0 else "^"*-dr
        h = ">"*dc if dc > 0 else "<"*-dc

        if dc > 0 and (target_r,curr_c) in pad_map:
            out += v+h
        elif (curr_r,target_c) in pad_map:
            out += h+v
        else:
            out += v+h
        out += "A"
        curr_r, curr_c = target_r, target_c
    return out

out = 0
for line in lines:
    s = expand(expand(expand(line, nums), dirs), dirs)
    out += int(line[:-1]) * len(s)
print(out)

def sub_paths(s, pad):
    return [sub+"A" for sub in expand(s, pad).split("A")][:-1]

out = 0
for line in lines:
    cnt = Counter(sub_paths(line, nums))

    for _ in range(25):
        next_cnt = Counter()
        for val, cnt in cnt.items():
            for sub_path in sub_paths(val, dirs):
                next_cnt[sub_path] += cnt
        cnt = next_cnt

    out += int(line[:-1]) * sum(len(k)*v for k,v in cnt.items())
print(out)
