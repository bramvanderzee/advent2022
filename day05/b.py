from collections import deque

stacks = [deque() for _ in range(9)]
stacksDone = False
moves = []
with open('input.txt') as f:
    for l in f:
        line = l.strip('\n')
        if line == '':
            stacksDone = True
            continue
        if stacksDone:
            n, f, t = line.split()[1::2]
            moves.append([n, f, t])
        else:
            row = list(line)[1::4]
            for i, n in enumerate(row):
                if n != ' ':
                    if ord(n) > 64:
                        stacks[i].append(n)

for move in moves:
    n, f, t = [int(n) for n in move]
    crane = deque()
    for _ in range(n):
        crane.appendleft(stacks[f-1].popleft())
    stacks[t-1].extendleft(crane)

print(stacks)
print(''.join([n.popleft() for n in stacks]))
