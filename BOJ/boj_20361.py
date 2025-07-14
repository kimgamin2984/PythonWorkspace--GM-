n,x,k = map(int,input().split())
ans = [0] * n
ans[x-1] = 1
for i in range(k):
    a,b = map(int,input().split())
    ans[a-1],ans[b-1] = ans[b-1],ans[a-1]
print(ans.index(1)+1)