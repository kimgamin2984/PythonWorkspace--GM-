import sys

n = int(sys.stdin.readline())
a = []
b = []
c = 1

for _ in range(n):
    d = int(sys.stdin.readline())
    while c <= d:
        a.append(c)
        b.append('+')
        c += 1
    if a[-1] == d:
        a.pop()
        b.append('-')
    else:
        print('NO')
        exit()

[print(i) for i in b]