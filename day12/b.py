import sys
from collections import deque

V = {}
start = None
end = None
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for y,l in enumerate(f):
        for x, char in enumerate(l.strip()):
            if char == 'S':
                start = (x, y)
                char = 'a'
            elif char == 'E':
                end = (x, y)
                char = 'z'
            V[(x, y)] = ord(char)

def getadj(coords):
    value = V[coords]
    x, y = coords
    adj = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    result = set()
    for coord in adj:
        if coord in V:
            if not V[coord] > value+1:
                result.add(coord)
    return result

def dfs(start):
    stack = deque([[start]])
    seen = []
    while stack:
        path = stack.popleft()
        coord = path[-1]
        if coord not in seen:
            adj = getadj(coord)
            for n in adj:
                new_path = list(path)
                new_path.append(n)
                stack.append(new_path)
                if n == end:
                    return len(path)
            seen.append(coord)

shortest = 1e9
for k, v in V.items():
    if chr(v) == 'a':
        plen = dfs(k)
        if plen:
            best = min(plen, shortest)
            if best != shortest:
                print(best)
                shortest = best 
print(dfs(start))
print(shortest)
