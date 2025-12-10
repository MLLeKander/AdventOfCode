import scipy
import numpy as np
import re

with open("10.in") as f:
    lines = [l for l in f.readlines()]

def toggle(tup, ndxes):
    lst = list(tup)
    for ndx in ndxes:
        lst[ndx] ^= True
    return tuple(lst)

def find_nums(s):
    return [int(x) for x in re.findall(r"\d+", s)]

def solve1(code, ops):
    visited = set()
    target = tuple(x == "#" for x in code)

    cnt = 0
    q = [tuple([False] * len(code))]
    while len(q) > 0:
        next_q = []
        for item in q:
            if item == target:
                return cnt

            for op in ops:
                n = toggle(item, op)
                if n not in visited:
                    visited.add(n)
                    next_q.append(n)

        q = next_q
        cnt += 1
    print("?", code, ops)

def incr(tup, ndxes):
    lst = list(tup)
    for ndx in ndxes:
        lst[ndx] += True
    return tuple(lst)

def solve2(jolt, ops):
    targets = find_nums(jolt)
    
    A = np.zeros((len(targets), len(ops)))
    for op_ndx, op in enumerate(ops):
        for x in op:
            A[x, op_ndx] = 1
    bounds = [(0, None)] * len(ops)

    c = [1] * len(ops)
    result = scipy.optimize.linprog(c, A_eq=A, b_eq=targets, bounds=bounds, integrality=1)
    return round(result.fun)

    """
    o_symbols = sympy.symbols(" ".join(f"x{o_ndx}" for o_ndx in range(len(ops))))
    d = {t_ndx: 0 for t_ndx in range(len(targets))}
    for o_ndx, op in enumerate(ops):
        for t_ndx in op:
            d[t_ndx] = d[t_ndx] + o_symbols[o_ndx]

    eqs = [sympy.Eq(v, targets[k]) for k, v in d.items()]
    solutions = sympy.linsolve(eqs, o_symbols)
    solution = sum(list(solutions)[0])
    # Crap, this still has free variables..
    """

    """
    Recursive DFS, fails...
    state = [0] * len(targets)
    def recur(ndx):
        if state == targets:
            return 0
        elif ndx == len(ops):
            return 1e100

        op = ops[ndx]
        cnt = 0
        result = 1e100
        while all(state[x] <= targets[x] for x in op):
            result = min(result, recur(ndx+1))
            for x in op:
                state[x] += 1

            cnt += 1
        for x in op:
            state[x] -= cnt

        return result
    return recur(0)
    """

    """
    BFS fails...
    visited = set()
    target = tuple(find_nums(jolt))

    cnt = 0
    q = [tuple([0] * len(code))]
    while len(q) > 0:
        next_q = []
        for item in q:
            if item == target:
                return cnt

            for op in ops:
                if any(item[x] == target[x] for x in op):
                    continue
                n = incr(item, op)
                if n not in visited and all(a <= b for a,b in zip(n, target)):
                    visited.add(n)
                    next_q.append(n)

        q = next_q
        cnt += 1
    """

ans2 = ans1 = 0
for line in lines:
    code, *ops, jolt = line.split()
    code = code[1:-1]
    ops = [find_nums(op) for op in ops]
    jolt = jolt[1:-1]
    ans1 += solve1(code, ops)
    ans2 += solve2(jolt, ops)
print(ans1)
print(ans2)
