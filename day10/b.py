import sys
from collections import deque, defaultdict

instructions = deque()
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        line = l.strip().split()
        instructions.append(line)

cycle = 0
running = True
register = defaultdict(int)
stack = defaultdict(list)
stacksize = 0
register['x'] = 1
row = ''
screen = []

while running:
    if abs(cycle%40 - register['x']) < 2:
        row += '#'
    else:
        row += '.'

    if len(row) == 40:
        screen.append(row)
        print(row)
        row = ''

    if len(instructions) > 0 and stacksize == 0:
        cmd = instructions.popleft()
        if cmd[0] == 'noop':
            pass
        elif cmd[0].startswith('add'):
            pos = cmd[0][3:]
            num = int(cmd[1])
            stack[cycle+1].append((pos, num))
            stacksize += 1
    else:
        if stacksize < 1:
            running = False

        for cmd in stack[cycle]:
            pos, num = cmd
            register[pos] += num
            stacksize -= 1

    #print(cycle, len(instructions), stacksize, dict(register))
    cycle += 1
