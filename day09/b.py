import sys
from collections import defaultdict

def move(self, other):
    hx, hy = other
    tx, ty = self

    if abs(hx-tx) > 1 or abs(hy-ty) > 1:
        tx += 1 if hx-tx > 0 else -1 if hx-tx < 0 else 0
        ty += 1 if hy-ty > 0 else -1 if hy-ty < 0 else 0

    return (tx, ty)

hx, hy = 0,0
tails = [(0,0) for _ in range(10)]
seen = defaultdict(int)
seen[(0,0)] = 1
D = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        i = l.strip()
        d, n = i.split()
        n = int(n)
        dx, dy = D[d]
        for _ in range(n):
            hx += dx
            hy += dy
            tails[0] = (hx, hy)
            for index in range(1, len(tails)):
                head = tails[index-1]
                tail = tails[index]
                tx, ty = move(tail, head)
                tails[index] = (tx, ty)
            seen[tails[-1]] += 1


c = 0
for x in seen.values():
    if x > 0:
        c += 1
print(c)

