n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key = lambda x: [x[1],x[0]])
[print(i[0],i[1]) for i in a]