import random as rd

rsp = ("가위", "바위", "보")
table = (('비겼습니다.','당신이 이겼습니다.','당신이 졌습니다'),
         ('당신이 졌습니다.','비겼습니다.','당신이 이겼습니다.'),
         ('당신이 이겼습니다.','당신이 졌습니다.','비겼습니다.'))
score = 0
game = 0

while True:
    while True:
        user_input = input("\n무엇을 내시겟습니까?(가위, 바위, 보): ")
        if user_input.replace(' ','') != '가위' and user_input.replace(' ','') != '바위' and user_input.replace(' ','') != '보':
            print('입력오류')
        else:
            break
    com_input = rd.choice(rsp)
    print(f"나 : {user_input.replace(' ','')}")
    print(f"computer : {com_input}")
    print(table[rsp.index(com_input)][rsp.index(user_input.replace(' ',''))])
    if table[rsp.index(com_input)][rsp.index(user_input.replace(' ',''))] == '당신이 이겼습니다.':
        score += 1
    if user_input.replace(' ','') != com_input:
        game += 1
        print(f'점수: {score}점')
        print(f'승률: {round(score/game*100,1)}% ({score}/{game})')
        while True:
            r = input('\n다시 하시겠습니까? (y/n): ')
            if r.replace(' ','') == 'n' or r.replace(' ','') == 'N' or r.replace(' ','') == 'y' or r.replace(' ','') == 'Y':
                break
            else:
                print('입력오류')
        if r.replace(' ','') == 'n' or r.replace(' ','') == 'N':
            break