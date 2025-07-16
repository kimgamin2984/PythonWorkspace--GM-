a,b = '',0
n,m,k = map(int,input().split())
l = list(map(int,input().split()))
l1 = l
l1 = sorted(l1)
for i in range(n):
    if b+l1[i]-2+m <= k:
        b += l1[i]-1
    else:
        break
if i <= k:
    for j in range(i):
        a += '0'*(l1[j]-1)+str(l.index(l1[j])+1)
if a.count('0')+k-len(a) > m:
    print(-1)
else:
    a += '0'*(k-len(a))
    print(' '.join(a))