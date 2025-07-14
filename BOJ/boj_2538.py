graph = [[0]*100 for _ in range(100)]
result = 0

for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(10):
        graph[99-y-i][x:x+10] = [1]*10
for j in graph:
    result += j.count(1)
print(result)