num1 = int(input('숫자 입력 : '))
num2 = int(input('숫자 입력 : '))

# 더 큰 값이 뭔가? 찾아내는 과정은 사실 필요 없다.


for i in range(1, num2+1) :
    # num1, num2를 동시에 나눠떨어뜨리는가?
    if (num1 % i == 0) and (num2 % i) == 0:
        # i는 num1, num2를 둘 다 나눠줌
        # 공약수 발견
        print(i)