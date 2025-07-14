import sys
n = int(sys.stdin.readline().rstrip())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
o = list(set(l))
d = {j: i for i, j in enumerate(o)}
m = list(map(list,zip(o,[0 for i in l])))
for i in l:
    m[d[i]][1] += 1
m.sort(key=lambda x: (x[1],x[0]),reverse=True)
for i in range(len(m)-1):
    if m[i][1] != m[i+1][1]:
        m = m[:i+1]
        break
if sum(l) >=  0:
    sys.stdout.write(f'{int(sum(l)/n+0.5)}\n')
else:
    sys.stdout.write(f'{int(sum(l)/n-0.5)}\n')
sys.stdout.write(f'{sorted(l)[n//2]}\n')
if len(m) != 1:
    if m[0][1] == m[1][1]:
        sys.stdout.write(f'{m[-2][0]}\n')
    else:
        sys.stdout.write(f'{m[-1][0]}\n')
else:
    sys.stdout.write(f'{m[0][0]}\n')
sys.stdout.write(f'{max(l)-min(l)}\n')