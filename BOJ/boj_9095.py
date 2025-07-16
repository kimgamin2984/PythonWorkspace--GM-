d = {1:1,2:2,3:4}
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1,n+1):
        try:
            d[i]
        except:
            d[i] = d[i-3]+d[i-2]+d[i-1]
    print(d[n])