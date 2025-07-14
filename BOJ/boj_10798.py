a = []
[a.append(list(input())) for _ in range(5)]
for i in range(5):
    while len(a[i]) != 15:
        a[i].append('')
for i in range(15):
    for j in range(5):
        print(a[j][i],end='')