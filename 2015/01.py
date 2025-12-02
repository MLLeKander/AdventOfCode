with open("01.in") as f:
    inp = [line.strip() for line in f.readlines()]

print(inp[0].count("(")-inp[0].count(")"))

curr = 0
for ndx, ch in enumerate(inp[0]):
    if ch == "(":
        curr += 1
    else:
        curr -= 1
        if curr < 0:
            print(ndx+1)
            break
