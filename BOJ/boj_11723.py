import sys
s = set()
m = int(sys.stdin.readline().rstrip())
for i in range(m):
    c = sys.stdin.readline().rstrip().split()
    if len(c) == 2:
        c[1] = int(c[1])
    if c[0] == 'add':
        s.add(c[1])
    if c[0] == 'remove':
        s.discard(c[1])
    if c[0] == 'check':
        if c[1] in s:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    if c[0] == 'toggle':
        if c[1] in s:
            s.remove(c[1])
        else:
            s.add(c[1])
    if c[0] == 'all':
        s = set([i+1 for i in range(20)])
    if c[0] == 'empty':
        s = set()