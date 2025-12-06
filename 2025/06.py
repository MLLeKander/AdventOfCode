import numpy as np

with open("06.in") as f:
    lines = [l[:-1] for l in f.readlines()]

ans2 = ans1 = 0
for line in zip(*[line.split() for line in lines]):
    if line[-1] == "+":
        ans1 += sum(int(x) for x in line[:-1])
    else:
        out = 1
        for x in line[:-1]:
            out *= int(x)
        ans1 += out

arr = np.array([list(line) for line in lines])
cols = list(np.where(arr[-1,:] != ' ')[0]) + [len(lines[0])]
for c0, c1 in zip(cols, cols[1:]):
    subarr = arr[:,c0:c1]
    if np.all(subarr[:,-1] == " "):
        subarr = subarr[:,:-1]
    nums = [int(''.join(line)) for line in subarr[:-1,:].T.tolist()]
    if subarr[-1,0] == "+":
        ans2 += sum(nums)
    else:
        out = 1
        for x in nums:
            out *= x
        ans2 += out

print(ans1, ans2)
