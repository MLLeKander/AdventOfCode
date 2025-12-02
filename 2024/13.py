import re
import numpy as np

with open("13.in") as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")

def group_every_n(l, n):
  return [l[i:i + n] for i in range(0, len(l), n)]

def solve(x1,y1,x2,y2,x,y,max_press):
    A, B = np.linalg.solve([[x1,x2],[y1,y2]], [x,y])
    A = int(np.round(A))
    B = int(np.round(B))
    if max_press is not None:
        if A > max_press or B > max_press:
            return None, None
    return A, B

out1 = 0
out2 = 0
for a,b,c,_ in group_every_n(lines, 4):
    _, x1, _, y1 = re.split(r'[+,]', a)
    _, x2, _, y2 = re.split(r'[+,]', b)
    _, x, _, y = re.split(r'[=,]', c)

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x = int(x)
    y = int(y)

    A, B = solve(x1,y1,x2,y2,x,y,100)
    if A is not None and A * x1 + B * x2 == x and A * y1 + B * y2 == y:
        out1 += 3 * A + B

    x += 10000000000000
    y += 10000000000000
    A, B = solve(x1,y1,x2,y2,x,y,None)
    if A is not None and A * x1 + B * x2 == x and A * y1 + B * y2 == y:
        out2 += 3 * A + B


print(out1)
print(out2)

"""
A * x1 + B * x2 = x
A * y1 + B * y2 = y


A * y1 + (A * x1 - x) * y2 / x2 = y
A * y1 + (A * x1 * y2 / x2 - x * y2 / x2 = y
A * (y1 + x1 * y2 / x2) = y + x * y2 / x2
A = y + x * y2 / x2 / (y1 + x1 * y2 / x2)


(A * y1 - y) / y2 = (A * x1 - x) / x2
(A * y1 - y) * x2 = (A * x1 - x) * y2
A * y1 * x2 - y * x2 = A * x1 * y2 - x * y2
A * y1 * x2 - A * x1 * y2 = y * x2 - x * y2
A * (y1 * x2 - x1 * y2) = y * x2 - x * y2
A = (y * x2 - x * y2) / (y1 * x2 - x1 * y2)
B = (A * x1 - x) / x2
"""



