
import itertools

with open("09.in") as f:
    lines = [l for l in f.readlines()]

nums = [list(map(int, line.split(","))) for line in lines]

# poly = shapely.Polygon(nums)
def is_okay(rax, ray, rbx, rby):
    """
    return poly.contains(shapely.box(rax, ray, rbx, rby))
    """
    for (ax,ay), (bx,by) in zip(nums, nums[1:] + [nums[0]]):
        ax, bx = sorted([ax, bx])
        ay, by = sorted([ay, by])
        if ax == bx:
            if rax < ax < rbx and by > ray and ay < rby:
                return False
        else:
            if ray < ay < rby and bx > rax and ax < rbx:
                return False
    return True

ans2 = ans1 = 0
for (ax,ay), (bx,by) in itertools.combinations(nums, 2):
    ax, bx = sorted([ax, bx])
    ay, by = sorted([ay, by])
    area = (bx-ax+1)*(by-ay+1)

    ans1 = max(ans1, area)
    if area > ans2 and is_okay(ax, ay, bx, by):
        ans2 = area
print(ans1, ans2)


# This is all wrong, 92902 is the wrong answer lol
# 100%|████████████████████████████████████████████████████████████████████| 98396/98396 [48:11<00:00, 34.03it/s]
# 92902
"""
from skimage.morphology import flood_fill
from tqdm import tqdm
import numpy as np
import shapely

width = max(x[0] for x in nums)+2
height = max(x[1] for x in nums)+2

board = np.zeros((width, height), dtype=np.uint8)
for (ax, ay), (bx, by) in zip(nums, nums[1:] + [nums[0]]):
    if ax == bx:
        for y in range(*sorted([ay,by])):
            board[ax][y] = 1
    else:
        assert ay == by
        for x in range(*sorted([ax,bx])):
            board[x][ay] = 1

board = flood_fill(board, (0,0), 2)

def get_max_area(heights):
    n = len(heights)
    s = []
    res = 0

    for i in range(n):
        while s and heights[s[-1]] >= heights[i]:
            tp = s.pop()

            # Width between previous smaller (stack top) and current index
            width = i if not s else i - s[-1] - 1

            res = max(res, heights[tp] * width)
        s.append(i)

    while s:
        tp = s.pop()
        width = n if not s else n - s[-1] - 1
        res = max(res, heights[tp] * width)

    return res

heights = [0] * height
ans2 = 0
for x in tqdm(range(width)):
    for y in range(height):
        if board[x][y] != 2:
            heights[y] += 1
        else:
            heights[y] = 0

    ans2 = max(ans2, get_max_area(heights))
    #stack = []
    #tmp = 0
    #for y in range(height):
    #    pass
    #    while len(stack) > 0 and heights[s[-1]] >= heights[y]:
    #        top = stack.pop()
print(ans2)
"""


# This is also wrong lol
"""
def read(arr, ndx):
    print(ndx, len(arr))
    if ndx < 0:
        return arr[ndx + len(arr)]
    if ndx >= len(arr):
        return arr[ndx - len(arr)]
    return arr[ndx]

def search_delta(ndx, xy_ndx, delta):
    print(search_delta, ndx, xy_ndx, delta)
    start_val = nums[ndx][xy_ndx]

    while read(nums, ndx)[xy_ndx] == start_val:
        ndx += delta

    if read(nums, ndx)[xy_ndx] < start_val:
        while read(nums, ndx)[xy_ndx] <= start_val:
            print(ndx, read(nums,ndx))
            ndx += delta
    else:
        while read(nums, ndx)[xy_ndx] >= start_val:
            ndx += delta
    return read(nums, ndx)[1 - xy_ndx]

def search(ndx, delta):
    x, y = nums(ndx)
    if read(nums, ndx+delta)[0] == x:
        if read(nums, ndx+2*delta)[0] < x:
            while read(nums, ndx)[0] <= x:
                ndx += delta
        else:
            while read(nums, ndx)[0] >= x:
                ndx += delta
    else:
        if read(nums, ndx+2*delta)[1] < y:
            while read(nums, ndx)[1] <= y:
                ndx += delta
        else:
            while read(nums, ndx)[1] >= y:
                ndx += delta

ans2 = 0
for ndx in tqdm(range(len(nums))):
    ay = search_delta(ndx, 0, 1)
    ax = search_delta(ndx, 1, 1)
    by = search_delta(ndx, 0, -1)
    bx = search_delta(ndx, 1, -1)
    ans2 = max(ans2, abs(ax-bx)*abs(ay-by))
print(ans2)
"""
