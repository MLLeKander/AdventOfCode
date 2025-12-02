import hashlib
import itertools

with open("04.in") as f:
    inp = [line.strip() for line in f.readlines()]

for ndx in itertools.count(1):
    if hashlib.md5((inp[0] + str(ndx)).encode()).hexdigest().startswith("000000"):
        print(ndx)
        break
