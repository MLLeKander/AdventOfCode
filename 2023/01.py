import re

with open("01.in") as f:
    lines = [line.strip() for line in f.readlines()]

out1 = 0
out2 = 0
words = [("one","1"), ("two","2"), ("three","3"), ("four","4"), ("five","5"), ("six","6"), ("seven","7"), ("eight","8"), ("nine","9")]
for line in lines:
    x = re.sub(r"[^\d]", "", line)
    out1 += int(x[0]+x[-1])

    x = ""
    for lndx in range(len(line)):
        if line[lndx].isnumeric():
            x += line[lndx]
        else:
            for word, digit in words:
                if line[lndx:].startswith(word):
                    x += digit
    out2 += int(x[0]+x[-1])

print(out1)
print(out2)
