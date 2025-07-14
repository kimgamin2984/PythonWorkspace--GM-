import sys
a = []
n = int(sys.stdin.readline())
counter = [0] * 31
for i in range(n):
    counter[int(sys.stdin.readline())] += 1
for i in range(1,31):
    for j in range(counter[i]):
        a.append(i)
a = a[int(n * 0.15 + 0.5):n-int(n * 0.15 + 0.5)]
if len(a) == 0:
    print(0)
else:
    if sum(a)/len(a) - int(sum(a)/len(a)) >= 0.5:
        print(int(sum(a)/len(a))+1)
    else:
        print(int(sum(a)/len(a)))