import re
import string

with open("05.in") as f:
    inp = [line.strip() for line in f.readlines()]

out = 0
for line in inp:
    vowel_count = sum(line.count(v) for v in "aeiou")
    dbl_count = sum(line.count(a+a) for a in string.ascii_lowercase)
    bad_count = sum(line.count(s) for s in ["ab","cd","pq","xy"])
    if vowel_count >= 3 and dbl_count >= 1 and bad_count == 0:
        out += 1
print(out)

out = 0
for line in inp:
    if re.search(r"(..).*\1", line) and re.search(r"(.).\1", line):
        out += 1
print(out)
