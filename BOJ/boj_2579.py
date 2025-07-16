n = int(input())
l1 = [0]*(n+2)
l2 = [0]*(n+2)
s = [int(input()) for i in range(n)]
for i in range(n):
    l1[i+2] = max([l1[i],l2[i]])+s[i]
    l2[i+2] = max([l1[i+1],l2[i+2]])+s[i]
print(max([l1[-1],l2[-1]]))