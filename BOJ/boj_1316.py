def check(a):
    b = []
    for i in range(len(a)):
        if b.count(a[0]) == 0:
            b.append(a.pop(0))
        else:
            if b[-1] != a[0]:
                return 0
            else:
                a.pop(0)
    return 1
n = int(input())
b = 0
for _ in range(n):
    a = list(input())
    b += check(a)
print(b)