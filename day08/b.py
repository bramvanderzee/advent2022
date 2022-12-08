import sys
from collections import defaultdict

G = []

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        x = l.strip()
        G.append([int(n) for n in x])

def score(row, tree):
    score = 0
    for t in row:
        score += 1
        if t >= tree:
            break

    return score

scores = defaultdict(int)
for y, row in enumerate(G):
    for x, tree in enumerate(row):
        left = list(reversed(G[y][:x]))
        right = G[y][x+1:]
        up =  list(reversed([G[yo][x] for yo in range(y)]))
        down = [G[yo][x] for yo in range(y+1, len(G))]

        l = score(left, tree)
        r = score(right, tree)
        u = score(up, tree)
        d = score(down, tree)
        print(x, y, tree, u*d*l*r, u, l, d, r, up, left, down, right)
        scores[(x, y)] = u*d*l*r



best = max(scores.values())
print(best)
