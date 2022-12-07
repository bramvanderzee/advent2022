import sys
from collections import deque, defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    cur_path = deque()

    sizes = defaultdict(int) # store path and size here

    for l in f:
        x = l.strip()
        cmd = x.split()

        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    cur_path.pop()
                else:
                    cur_path.append(cmd[2])
            elif cmd[1] == 'ls':
                pass
        elif cmd[0] == 'dir':
            # dir
            pass
        else:
            # file
            upd_path = []
            for p in cur_path:
                upd_path.append(p)
                path = '/'.join(upd_path)
                sizes[path] += int(cmd[0])

    ans = 0
    for v in sizes.values():
        if v <= 100000:
            ans += v
    print(ans)
