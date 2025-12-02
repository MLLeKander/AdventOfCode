import re

with open("03.txt") as f:
    c = f.read()

print(sum(int(a)*int(b) for a,b in re.findall("mul\((\d{1,3}),(\d{1,3})\)", c)))

flag = True
out = 0
for dont, do, a, b in re.findall("(don't)\(\)|(do)\(\)|mul\((\d{1,3}),(\d{1,3})\)", c):
    if do:
        flag = True
    elif dont:
        flag = False
    elif flag:
        out += int(a) * int(b)
print(out)
