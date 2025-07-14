n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    if a[-1] == 0:
        a.pop()
        a.pop()
print(sum(a))