def getScore(ch):
    s = ord(ch)-96
    if s < 0:
        s += 58
    return s

score = 0
groups = []
with open('input.txt') as f:
    group = []
    for l in f:
        r = l.strip()
        group.append(r)
        if len(group) == 3:
            groups.append(group)
            group = []

for group in groups:
    g1, g2, g3 = set(group[0]), set(group[1]), set(group[2])
    for c in g1:
        if c in g2:
            if c in g3:
                score += getScore(c)
                break

print(score)
