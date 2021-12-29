for i in range(1,11):
    print(i)

print('------------------------')
# range의 마지막에 넣는 숫자만큼 한바튀를 돌 때마다 더해줌 (증감폭 설정)
for i in range (20, 10, -1):
    print(i)

print('------------------------')
# reversed : 내부에 들어간 목록을 역순으로 바꿔줌.
for i in reversed(range(11,21)):
    print(i)
    
print('------------------------')
for i in range(0,5) :
    print('안녕하세요')
    
print('------------------------')

# range의 출발점을 안 잡으면 0 에서 자동 출발
# 단순 횟수 조정 : range(횟수)로 작성하면 더 편리함
for i in range(5) :
    print('안녕하세요')
    
print('------------------------')    
    
for i in range(2, 21, 2):
    print(i)
    
for i in range(10):
    print((i+1)*2)
    
