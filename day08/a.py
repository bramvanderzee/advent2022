import sys

G = []

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        x = l.strip()
        G.append([int(n) for n in x])

seen = set()
for y, row in enumerate(G):
    for x, tree in enumerate(row):
        if (x, y) not in seen:
            if x == 0 or y == 0:
                seen.add((x, y))
            elif y == len(G)-1 or x == len(row)-1:
                seen.add((x, y))
            else:
                if max(row[:x]) < tree or max(row[x+1:]) < tree:
                    seen.add((x, y))
                else:
                    col = [G[n][x] for n in range(len(G))]
                    if max(col[:y]) < tree or max(col[y+1:]) < tree:
                        seen.add((x, y))

print(len(G), len(G[0]))
print(seen)
print(len(seen))
