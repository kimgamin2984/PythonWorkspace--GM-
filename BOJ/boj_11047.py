n,k = map(int,input().split())
r = 0
c = [int(input()) for i in range(n)]
for i in range(n):
    if c[i] > k:
        c = c[:i]
        break
c = list(reversed(c))
for i in c:
    r += k//i
    k %= i
print(r)