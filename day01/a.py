cals = []

with open('input.txt') as f:
    elf = []
    for l in f:
        x = l.strip()
        if x == "":
            cals.append(sum(elf))
            elf = []
        else:
            elf.append(int(x))

print(cals)
print(max(cals))
