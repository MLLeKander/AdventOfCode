with open("04.txt") as f:
    lines = [line.strip() for line in f.readlines()]

cols = len(lines[0])
bufflen = cols+1
lines = [line+("|"*bufflen) for line in lines]
out = 0
flat = ''.join(lines)

def stride(l):
    s = ""
    for x in range(min(l,bufflen+cols)):
        s += flat[x::l] + "+"
    return s

X = "XMAS"
S = "SAMX"

def search(l, desc):
    s = stride(l)
    print(desc, s)
    print("X", s.count(X), "S", s.count(S))
    return s.count(X) + s.count(S)

out = 0
out += search(1, "ROW")
out += search(cols+bufflen, "COL")
out += search(cols+bufflen+1, "DR ")
out += search(cols+bufflen-1, "DL ")
print(out)
