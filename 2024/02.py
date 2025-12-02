result = 0
lines = open("02.in").readlines()
lines = [[int(x) for x in line.strip().split()] for line in lines]

def is_safe(line):
    if line[0] < line[1]:
        for a, b in zip(line, line[1:]):
            if b - a <= 0 or b - a > 3:
                return False
    else:
        for b, a in zip(line, line[1:]):
            if b - a <= 0 or b - a > 3:
                return False
    return True

print(sum(is_safe(line) for line in lines))

def is_safe2(line):
    for ndx in range(len(line)):
        if is_safe(line[:ndx] + line[ndx+1:]):
            return True
    return False

print(sum(is_safe2(line) for line in lines))
