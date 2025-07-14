n = int(input())
if n == 4 or n == 7:
    print(-1)
else:
    for i in range(5):
        if n%5 == 0:
            break
        n -= 3
    print(i+n//5)