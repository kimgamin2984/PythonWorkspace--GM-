import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if a[x][y] != 1:
        return
    a[x][y] = 0
    for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
        dfs(x+dx,y+dy)
t = int(input())
for i in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    a = [[0]*m for i in range(n)]
    for i in range(k):
        b,c = map(int,input().split())
        a[c][b] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)