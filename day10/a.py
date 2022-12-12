import sys
from collections import deque, defaultdict

instructions = deque()
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        line = l.strip().split()
        instructions.append(line)

cycle = 1
running = True
register = defaultdict(int)
stack = defaultdict(list)
stacksize = 0
register['x'] = 1
ans = 0
while running:
    if cycle in [20, 60, 100, 140, 180, 220]:
        ans += register['x']*cycle
        print(ans, register['x']*cycle)

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

    print(cycle, len(instructions), stacksize, dict(register))
    cycle += 1

print(ans)
