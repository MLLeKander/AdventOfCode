import re

def get_nums(s):
    return [int(x) for x in re.findall(r"\d+", s)]

presents = []
queries = []
with open("12.in") as f:
    while f:
        line = f.readline().strip()
        if line == "":
            break
        elif "x" in line:
            w, h, *spec = get_nums(line)
            queries.append((w,h,spec))
        else:
            present = [f.readline().strip() for _ in range(3)]
            present = sum(x.count("#") for x in present)
            presents.append(present)
            f.readline()

ans1 = 0
for w, h, spec in queries:
    if w*h > sum(cnt*p for cnt, p in zip(presents, spec)):
        ans1 += 1
print(ans1)
