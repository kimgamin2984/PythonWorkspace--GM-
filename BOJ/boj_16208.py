n = int(input())
a = list(map(int,input().split()))
a.sort()
s = sum(a)
r = 0
for i in a:
    s -= i
    r += i * s
print(r)