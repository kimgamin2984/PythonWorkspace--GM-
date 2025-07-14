alphabet_count = [0]*26
alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

input = list(input().upper())
for i in range(26):
    alphabet_count[i] = input.count(alphabet[i])
if alphabet_count.count(max(alphabet_count)) >= 2:
    print('?')
else:
    print(alphabet[alphabet_count.index(max(alphabet_count))])