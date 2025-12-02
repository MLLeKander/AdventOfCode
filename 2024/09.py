with open("09.in") as f:
    inp = f.read().strip()
inp += "0"

desc = []
for ndx, (file, free) in enumerate(zip(inp[::2], inp[1::2])):
    file = int(file)
    free = int(free)
    if file > 0:
        desc.append((ndx, file))
    if free > 0:
        desc.append((None, free))

def make_disk(desc):
    disk = []
    for val, cnt in desc:
        disk.extend([val] * cnt)

    return disk

def make_checksum(disk):
    checksum = 0
    for ndx, c in enumerate(disk):
        if c is not None:
            checksum += ndx * c
    return checksum

disk = make_disk(desc)
rndx = len(disk)-1
for lndx in range(len(disk)):
    if lndx > rndx:
        break

    if disk[lndx] is None:
        disk[lndx], disk[rndx] = disk[rndx], None
        while disk[rndx] is None:
            rndx -= 1

print(make_checksum(disk))

curr_val = desc[-1][0]
rndx = len(desc)

def find_opening(rndx):
    size = desc[rndx][1]
    for i in range(rndx):
        if desc[i][0] is None and desc[i][1] >= size:
            return i
    return None

while curr_val > 0:
    rndx -= 1
    if desc[rndx][0] != curr_val:
        continue
    opening = find_opening(rndx)
    if opening is not None:
        remain_len = desc[opening][1] - desc[rndx][1]
        if remain_len == 0:
            desc[opening] = desc[rndx]
        else:
            desc[opening] = desc[rndx]
            desc.insert(opening+1, (None, remain_len))
            rndx += 1
        desc[rndx] = (None, desc[rndx][1])
    curr_val -= 1

print(make_checksum(make_disk(desc)))
#print(''.join(str(x) if x is not None else '.' for x in make_disk(desc)))
