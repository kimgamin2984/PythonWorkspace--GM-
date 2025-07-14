a = input()
b = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(8):
    try:
        a = a.replace(b[i],'*')
    except:
        pass
print(len(a))