count = 0

with open('input.txt') as f:
    for l in f:
        elf1, elf2 = l.strip().split(',')
        s1, e1 = elf1.split('-')
        s2, e2 = elf2.split('-')
        s1, s2, e1, e2 = int(s1), int(s2), int(e1), int(e2)
        
        r1 = set([n for n in range(s1, e1+1)])
        r2 = set([n for n in range(s2, e2+1)])

        i = r1.intersection(r2)
        if i:
            count += 1
print(count)
