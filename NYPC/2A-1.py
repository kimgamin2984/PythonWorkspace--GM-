import sys
input = sys.stdin.readline
n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
r = float('inf')
for i in range(n-k+1):
    m = l[i+k//2]
    c = 0
    for j in range(i,i+k):
        c += abs(l[j]-m)
    r = min(r,c)
print(r)