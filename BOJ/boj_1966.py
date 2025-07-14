t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    r = []
    o = m
    m = a[m]
    a[o] = 0
    while True:
        if max(a) <= m or max(a) == 0:
            break
        a1 = a[a.index(max(a)):]
        a2 = a[:a.index(max(a))]
        a = a1+a2
        a.pop(0)
        c += 1
    if max(a) == m:
        for i in a:
            if i == m or i == 0:
                r.append(i)
        print(r.index(0)+1+c)
    else:
        print(1+c)