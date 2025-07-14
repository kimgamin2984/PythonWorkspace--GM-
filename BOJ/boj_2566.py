a = []
for _ in range(9):
    a.append(list(map(int,input().split())))
    b = sum(a,[])

for i in range(9):
    if a[i].count(max(b)) >= 1:
        print(max(b))
        print(i+1,a[i].index(max(b))+1)