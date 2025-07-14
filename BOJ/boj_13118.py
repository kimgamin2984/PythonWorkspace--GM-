p = input()
x,y,r = input().split()
[print(p.split().index(x)+1) if p.find(x) != -1 else print(0)]