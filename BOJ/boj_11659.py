import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = [a[0]]+[0]*(n-1)
for i in range(1,n):
    b[i] = b[i-1]+a[i]
for i in range(m):
    c,d = map(int,input().split())
    if c == 1:
        sys.stdout.write(str(b[d-1])+'\n')
    else:
        sys.stdout.write(str(b[d-1]-b[c-2])+'\n')