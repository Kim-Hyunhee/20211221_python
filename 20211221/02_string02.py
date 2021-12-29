input_name = input('이름 입력 : ')

# input_name 자리에 변수 input_name에 들어있는 값을 집어넣자 (str 가공)

# f'string 활용 예시 (3.6 버전 이후에서만 사용 가능)
result1 = f'제 이름은 {input_name} 입니다.'


print(result1)


# 일반 format 함수 활용 예시 1
result2 = '제 이름은 {} 입니다.'.format(input_name)
print(result2)

input_age = int(input('나이 입력 : '))

# format 함수 활용 예시 2
result3 = '이름 :{0}, 나이 {1}세'.format(input_name,input_age)
print(result3)

# format 함수 활용 예시 3
result4 = '이름 : {name}, 나이 : {age}세'.format(name = input_name,age=input_age)
print(result4)