import random
import time

print('숫자 야구에 오신 것을 환영합니다')
time.sleep(1)
print('숫자 야구는 숫자 네 개의 조합을 맞히는 게 목표인 게임입니다')
time.sleep(2)
print('세부 규칙은 다음과 같습니다')
time.sleep(1)
print('1. 정답은 1에서 9 사이의 서로 다른 숫자 4개로 이루어진다')
time.sleep(2)
print('2. 숫자는 맞지만 위치가 틀린 경우는 볼이라고 한다')
time.sleep(2)
print('3. 숫자와 위치가 전부 맞은 경우는 스트라이크라고 한다')
time.sleep(2)
print('4. 숫자와 위치가 전부 틀린 경우는 아웃이라고 한다')
time.sleep(2)
print('5. 무엇이 볼이고 무엇이 스트라이크인지는 알려주지 않는다')
time.sleep(2)
print('6. 입력은 띄어쓰기로 구분한다 예시:1 2 3 4')
time.sleep(2)
print('그럼 시작하겠습니다.')
print()
time.sleep(1)

while True :
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    while b == a :
        b = random.randrange(1,10)
    c = random.randrange(1,10)
    while c == a or c == b :
        c = random.randrange(1,10)
    d = random.randrange(1,10)
    while d == a or d == b or d == c:
        d = random.randrange(1,10)

    answer = [str(a),str(b),str(c),str(d)]
    num = 0
    while True :
        num += 1

        trial = []
        trial = input(str(num)+'번째 시도: ').split()

        while len(trial) != 4 :
            print('올바른 답을 입력하세요')
            trial = input().split()

        if answer == trial :
            print('정답입니다',str(num)+'번째 시도만에 맞히셨습니다')
            print('다시 하시겠습니까? Y나 N을 입력해주세요')
            break

        def cor() :
            y = 0
            if answer[0] == trial[0] :
                y += 1
            if answer[1] == trial[1] :
                y += 1
            if answer[2] == trial[2] :
                y += 1
            if answer[3] == trial[3] :
                y += 1
            return y
        
        if answer.count(trial[0])+answer.count(trial[1])+answer.count(trial[2])+answer.count(trial[3])-cor() == 0 and cor() == 0 :
            print('아웃')
        else :
            print(str(answer.count(trial[0])+answer.count(trial[1])+answer.count(trial[2])+answer.count(trial[3])-cor())+'볼',str(cor())+'스트라이크')
            print()
    z = 0
    while True :
        z = input()
        if z == 'N' or z == 'n' :
            break
        elif z == 'Y' or z == 'y' :
            print('그럼 다시 시작하겠습니다')
            print()
            break
        else :
            print('올바른 문자를 입력하세요')
    if z == 'N' or z == 'n' :
        break