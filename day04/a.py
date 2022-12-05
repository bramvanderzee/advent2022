count = 0
with open('input.txt') as f:
    for l in f:
        elf1, elf2 = l.strip().split(',')
        s1, e1 = elf1.split('-')
        s2, e2 = elf2.split('-')
        s1, s2, e1, e2 = int(s1), int(s2), int(e1), int(e2)
        
        if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
            count += 1
            print('V', s1, e1, s2, e2)
        else:
            print('X', s1, e1, s2, e2)
            print(s1, s2, s1>=s2, e1, e2, e1<=e2)

print(count)
