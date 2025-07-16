m,n = map(int,input().split())
a = set([input()for i in range(m)])
b = set([input()for i in range(n)])
print(len(a&b))
[print(i)for i in sorted(list(a&b))]