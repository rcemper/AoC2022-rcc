#!/usr/bin/python
f = open("C:/GitHub/set2/6/input.txt", "r").read()

def part(pa,n) :
    for i in range(0, len(f) - n):
        t = 0
        for h in range(0, n):
            for r in range(h + 1, n):
                if f[i + h] == f[i + r]:
                    t = 1
        if t == 0:
            print('part ',pa,' = ',i + n)
            break
part(1,4)
part(2,14)
