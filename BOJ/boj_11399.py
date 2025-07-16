n = int(input())
a = sorted(list(map(int,input().split())))
b = 0
r = 0
for i in a:
    r += i + b
    b += i
print(r)