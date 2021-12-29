# 1번 5 * 4 별

for i in range(4):
    # 가로로 별 찍어주기 (5회 반복)
    for j in range(5):
        print('*',end = '')  # 일반 print : * 찍고 다음 줄로 내려감 => 어떻게 수정해야 줄을 안 내려갈 지 검색
    
    # 다음 줄로 줄 바꾸기만 실행
    print()  # 출력할 내용은 없이 줄만 바꿔지는가?
    
print('====================================')

# 2번 기본 삼각형

for i in range(5):
    for j in range(1):
        print('*', end = '') 
    
    print(i*'*')   

for i in range(5):
    for j in range(i+1):
        print('*', end = '')
        
    print()
    
print('====================================')

# 3번. 역삼각형

for i in range(5):
    for j in range(5-i):
        print('*',end = '')
        
    print()
    
print('====================================')

# 4번. 우측 정렬 삼각형 

for i in range(5):
    # 스페이스를 찍어주는 for
    for j in range(4-i):
        print(' ', end ='')
        
    # 별 찍어주는 for
    for k in range(i+1):
        print('*',end = '')
        
    # 스페이스와 별을 다 찍으면 다음 줄
    print()
