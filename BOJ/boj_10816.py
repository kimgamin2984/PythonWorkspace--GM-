import sys

n = int(sys.stdin.readline())
nl = sys.stdin.readline().split()
m = int(sys.stdin.readline())
ml = sys.stdin.readline().split()
dic = {}

for i in set(nl):
    dic[i] = 0

for i in nl:
    dic[i] += 1

for i in ml:
    try:
        sys.stdout.write(str(dic[i])+' ')
    except:
        sys.stdout.write('0 ')