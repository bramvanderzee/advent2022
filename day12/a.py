import sys
from collections import deque
G = {}
V = {}
start = None
end = None
maxx, maxy = 0, 0
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for y,l in enumerate(f):
        maxy = max(maxy, y)
        for x, char in enumerate(l.strip()):
            maxx = max(maxx, x)
            if char == 'S':
                start = (x, y)
                char = 'a'
            elif char == 'E':
                end = (x, y)
                char = 'z'
            G[(x, y)] = 1e9
            V[(x, y)] = ord(char)

def getadj(coords):
    value = V[coords]
    x, y = coords
    adj = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    result = set()
    for coord in adj:
        if coord in G:
            if not V[coord] > value+1:
                result.add(coord)
    return result

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
                print(len(path))
        seen.append(coord)
