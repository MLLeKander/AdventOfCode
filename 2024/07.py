import itertools

with open("07.in") as f:
    lines = [line.strip() for line in f.readlines()]

def add(a,b): return a+b
def mult(a,b): return a*b
def cat(a,b): return int(str(a)+str(b))

out = 0
out2 = 0
for line in lines:
    target, *args = line.split()
    target = int(target[:-1])
    args = [int(arg) for arg in args]

    def can_match(possible_ops):
        for ops in itertools.product(*[possible_ops] * (len(args)-1)):
            val = args[0]
            for arg, op in zip(args[1:], ops):
                val = op(val, arg)
                if val > target:
                    break
            if target == val:
                return True
        return False

    if can_match([add, mult]):
        out += target
    elif can_match([add, mult, cat]):
        out2 += target

print(out)
print(out+out2)
