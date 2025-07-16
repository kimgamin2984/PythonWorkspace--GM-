def fac(x):
    r = 1
    for i in range(x):
        r = r * (x - i)
    return r
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(fac(m)//(fac(n)*fac(m-n)))