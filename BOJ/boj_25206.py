dic = {'A+':45,'A0':40,'B+':35,'B0':30,'C+':25,'C0':20,'D+':15,'D0':10,'F':0,'P':0}
r = m = d = 0
for i in range(20):
    a,b,c = map(str,input().split())
    if c != 'P':
        d += int(b.strip('.0'))
    r += int(b.strip('.0')) * dic[c]
print(r/10/d)