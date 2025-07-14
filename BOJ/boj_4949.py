import re
while True:
    a = input()
    if a == '.':
        break
    a = re.sub(r'[^\[\]\(\)]','',a)
    while True:
        if a == re.sub(r'(\[\]|\(\))','',a):
            break
        else:
            a = re.sub(r'(\[\]|\(\))','',a)
    if a == '':
        print('yes')
    else:
        print('no')