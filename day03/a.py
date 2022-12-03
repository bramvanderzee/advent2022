def getScore(ch):
    s = ord(ch)-96
    if s < 0:
        s += 58
    return s

score = 0
with open('input.txt') as f:
    for l in f:
        r = l.strip()
        c1, c2 = r[:len(r)//2], r[len(r)//2:]
        for c in set(c1):
            if c in c2:
                score += getScore(c)
                print(r, c1, c2, c, score)

print(score)
