numbers = [1, 2, 3, 4]  # 목록을 표현하는 공간. numbers

# 원하는 위치의 숫자를 출력

# 맨 앞의 숫자
print(numbers[0])

# 마지막 숫자?  -1 번째.
# index 숫자를 음수로 넣으면 길이 -값 번째 아이템을 꺼내옴.
print(numbers[-2])


# 목록에 20 숫자 추가 => append : (맨 뒤에) 이어 붙이기
numbers.append(20)

# 숫자들이 들어있는 목록 => "안녕하세요" str 추가.
numbers.append("안녕하세요")


# 목록 안에 다른 목록 추가  (자료형에 상관 없다 : 목록 추가 가능)
numbers.append([50,60,70])

# 목록 자체를 출력
print(numbers)


numbers.remove('안녕하세요')

# 목록 자체를 출력
print(numbers)


numbers2 = range(1,10)  # 숫자 범위를 지정. 일종의 목록처럼 사용 가능
print(numbers2)
