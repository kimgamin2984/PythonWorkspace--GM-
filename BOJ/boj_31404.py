H,W = map(int,input().split())
R,C,D = map(int,input().split())
times = 0

A = []
for _ in range(H):
    A.append(list(map(int,list((input())))))
B = []
for _ in range(H):
    B.append(list(map(int,list((input())))))

visit = []
jido = [[1]*W for _ in range(H)]

while True:
    print(R,C,D,jido)
    if jido[R][C] == 1:
        jido[R][C] = 0
        visit = []
    else:
        visit.append([R,C])

    if visit == []:
        if (D + A[R][C]) % 4 == 0:
            R -= 1
            D = 0
            times += 1
        elif (D + A[R][C]) % 4 == 1:
            C += 1
            D = 1
            times += 1
        elif (D + A[R][C]) % 4 == 2:
            R += 1
            D = 2
            times += 1
        elif (D + A[R][C]) % 4 == 3:
            C -= 1
            D = 3
            times += 1
    else:
        if (D + B[R][C]) % 4 == 0:
            R -= 1
            D = 0
            times += 1
        elif (D + B[R][C]) % 4 == 1:
            C += 1
            D = 1
            times += 1
        elif (D + B[R][C]) % 4 == 2:
            R += 1
            D = 2
            times += 1
        elif (D + B[R][C]) % 4 == 3:
            C -= 1
            D = 3
            times += 1
    
    if visit.count([R,C]) or jido == [[0]*W for _ in range(H)] or not (0 <= R < H) or not (0 <= C < W):
        break
    
print(times-len(visit))