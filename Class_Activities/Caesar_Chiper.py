upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
	try:
		key = int(input('복호화 key를 입력하시오 (암호화의 경우 0을 입력하시오): '))
		break
	except:
		print('다시 입력하십시오')

string = input('평문/암호문을 입력하시오: ')

if key == 0:
    for key in range(26):
        print(f'{key:2}',end=' | ')
        for i in range(len(string)):
            if lower_alphabet.find(string[i]) == -1 and upper_alphabet.find(string[i]) == -1:
                print(string[i],end='')
            elif upper_alphabet.find(string[i]) >= 0:
                print(upper_alphabet[(upper_alphabet.find(string[i])+key)%26],end='')
            else:
                print(lower_alphabet[(lower_alphabet.find(string[i])+key)%26],end='')
        print()
else:
    for i in range(len(string)):
        if lower_alphabet.find(string[i]) == -1 and upper_alphabet.find(string[i]) == -1:
            print(string[i],end='')
        elif upper_alphabet.find(string[i]) >= 0:
            print(upper_alphabet[(upper_alphabet.find(string[i])-key)%26],end='')
        else:
            print(lower_alphabet[(lower_alphabet.find(string[i])-key)%26],end='')