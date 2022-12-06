from collections import deque

buff = deque()
with open('input.txt') as f:
    for l in f:
        x = l.strip()
        for i, c in enumerate(x):
            buff.append(c)
            if len(buff) == len(set(buff)) and len(buff) == 4:
                print(i+1, buff)
                break
            else:
                if len(buff) > 3:
                    buff.popleft()
