d = {1:1,2:1,3:1,4:2,5:2,6:3,7:4,8:5,9:7,10:9}
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(10,n+1):
        try:
            d[i]
        except:
            d[i] = d[i-5]+d[i-1]
    print(d[n])