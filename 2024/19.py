from collections import defaultdict
from tqdm import tqdm

with open("19.in") as f:
    lines = [line.strip() for line in f.readlines()]

towels = lines[0].split(", ")

cache = {}
def match_count(target):
    global cache
    cache = {}
    return _match_count(target, 0)

def _match_count(target, ndx):
    if ndx in cache:
        return cache[ndx]

    if ndx == len(target):
        return 1

    cnt = 0
    for towel in towels:
        if target.startswith(towel, ndx):
            cnt += _match_count(target, ndx+len(towel))

    cache[ndx] = cnt
    return cnt

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = defaultdict(TrieNode)
        self.name = ""
        self.cache = {}

    def add(self, s):
        if s == "":
            self.is_terminal = True
        else:
            child = self.children[s[0]]
            child.name = self.name + s[0]
            child.add(s[1:])

    def can_match(self, s, ndx=0):
        key = (s,ndx)
        if key not in self.cache:
            self.cache[key] = self._can_match(s, ndx)

        return self.cache[key]

    def _can_match(self, s, ndx):
        if ndx >= len(s):
            return self.is_terminal

        if s[ndx] in self.children and self.children[s[ndx]].can_match(s, ndx+1):
            return True
        
        if self.is_terminal and root_node.can_match(s, ndx):
            print("Exhausted", self.name)
            return True

        return False

root_node = TrieNode()
for towel in towels:
    root_node.add(towel)

matches = [match_count(line) for line in tqdm(lines[2:])]
print(sum(match > 0 for match in matches))
print(sum(matches))
