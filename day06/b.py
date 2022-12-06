from collections import deque

buff = [] 
SOP = None
SOM = None
with open('input.txt') as f:
    for l in f:
        x = l.strip()
        for i, c in enumerate(x):
            buff.append(c)
            if not SOP and i > 4 and len(buff[i-4:i]) == len(set(buff[i-4:i])):
                print(i, buff[i-4:i])
                SOP = i
            if i > 14 and len(buff[i-14:i]) == len(set(buff[i-14:i])):
                SOM = i
                print(SOM)
                break
