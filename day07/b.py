import sys
from collections import deque, defaultdict

sizes = defaultdict(int) # store path and size here

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    cur_path = deque()

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

used_space = sizes['/']
total_space = 70000000
needed_space = 30000000
to_free = -1*(total_space - used_space - needed_space)
print(to_free)
cur_folder = 10e9
for k, v in sizes.items():
    if to_free - v < 0:
        cur_folder = min(cur_folder, v)
print(cur_folder)
