line = open("02.in").read()

def is_invalid(x, reps):
    s = str(x)
    n = len(s)
    return n % reps == 0 and s == s[:n//reps]*reps

ranges = [list(map(int, r.split("-"))) for r in line.split(",")]
ans2 = ans1 = 0
for lo, hi in ranges:
    for x in range(lo, hi+1):
        if is_invalid(x, 2):
            ans1 += x
        for rep in [2,3,4,5,6,7,8,9,10]:
            if is_invalid(x, rep):
                if rep > 5:
                    print(x, rep)
                ans2 += x
                break
print(ans1, ans2)
