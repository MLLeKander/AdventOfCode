with open("02.in") as f:
    inp = [line.strip() for line in f.readlines()]

out = 0
out2 = 0
for line in inp:
    l,w,h = [int(x) for x in line.split("x")]
    out += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
    out2 += 2*min(l+w,w+h,h+l) + l*w*h
print(out)
print(out2)
