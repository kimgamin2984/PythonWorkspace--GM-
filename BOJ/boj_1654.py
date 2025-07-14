k,n = map(int,input().split())
l = [int(input()) for i in range(k)]
s = 1
e = max(l)
r = 0
while s <= e:
    m = (e+s)//2
    if sum(map(lambda x: x//m,l)) >= n:
        s = m + 1
        r = m
    else:
        e = m - 1
print(r)