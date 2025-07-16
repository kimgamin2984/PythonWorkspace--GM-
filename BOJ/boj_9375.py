t = int(input())
for i in range(t):
    d = {}
    s = set()
    r = 1
    n = int(input())
    for i in range(n):
        a = input().split()
        s.add(a[1])
        try:
            d[a[1]] += 1
        except:
            d[a[1]] = 1
    for i in list(s):
        r *= d[i]+1
    print(r-1)