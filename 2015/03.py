with open("03.in") as f:
    inp = [line.strip() for line in f.readlines()]

def walk(path):
    r,c = 0,0
    yield (r,c)
    for ch in path:
        if ch == ">":
            c += 1
        elif ch == "<":
            c -= 1
        elif ch == "v":
            r -= 1
        elif ch == "^":
            r += 1

        yield (r,c)

print(len(set(walk(inp[0]))))

print(len(set(walk(inp[0][::2])) | set(walk(inp[0][1::2]))))
