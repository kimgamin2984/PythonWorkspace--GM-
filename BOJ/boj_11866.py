n,k = map(int,input().split())
a = [i+1 for i in range(n)]
d = k-1
print('<',end='')
for i in range(n-1):
    print(a.pop(d),end=', ')
    d += k-1
    d %= len(a)
print(f'{a[0]}>')