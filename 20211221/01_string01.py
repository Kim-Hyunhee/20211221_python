str1 = 'Hello World!'

# str1 => string (문자열) => 여러 개의 문자가 이어붙여진 덩어리 => 배열 형태

print(str1)


# str1의 길이? => 배열이 몇 칸?
print(len(str1))

# str1의 4번째 글자?

# str 배열 => 배열의 위치는 0번 칸에서 출발 0,1,2,3 => 3번 칸을 추출해야 4번째 글자
char_5th = str1[3]

print(char_5th)

# 첫 글자 ~ 5번째 글자까지 부분 추출
# [출발지 : 도착지] => 도착지 숫자 직전까지만 추출

head_part_str = str1[0:5]
print(head_part_str)

# world만 추출
tail_part_str = str1[6:11]
print(tail_part_str)


test1 = str1[6:]
print(test1)

test2 = str1[:8]
print(test2)