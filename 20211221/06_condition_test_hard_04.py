income = int(input('소득 금액 입력 : '))

# 실 소득을 담게 될 변수
real_income = 0  # 숫자가 들어올 예정

#easy 버전
if income <= 1000 :
    # 실 소득? 6% 징수 => 세전 소득 * 0.94
    real_income = income * 0.94
elif income <= 4000:
    real_income = income * 0.85
elif income <= 8000:
    real_income = income * 0.76
else:
    real_income = income * 0.65


# hard 버전

if income <= 1000:
    real_income = income * 0.94
elif income <= 4000:
    # 실소득 계산 -> 1000 * 0.94 + 남은돈 * 0.85 => 합산
    real_income = 1000 * 0.94 + (income - 1000) * 0.85
elif income <= 8000:
    # 실소득 계산 -> 1000 * 0.94 + 3000 * 0.85 + 남은돈 * 0.76 => 합산
    real_income = 1000 * 0.94 + 3000 * 0.85 + (income - 4000) * 0.76
else:
    # 실소득 계산 -> 1000 * 0.94 + 3000 * 0.85 + 4000 * 0.76 + 남은돈 * 0.65 => 합산
    real_income = 1000 * 0.94 + 3000 * 0.85 + 4000 * 0.76 + (income - 8000) * 0.65

print(f'실 소득 금액 : {real_income}')


#  if 중첩 이용

if income <= 1000:
    real_income = income * 0.94
else:
    # 실 수입에 => 1000만원치 정산
    # 남은 금액이 얼마? 계산
    real_income = 1000 * 0.94
    
    rest_money = income - 1000
    
    # 추가 질문 : 남은돈이 3천 이하? => 둘째 구간(15%징수) 에서 정산 종료. 아니면? 추가 정산 필요.
    if rest_money <= 3000:
        # 실 소득 : 남은 돈 * 0.85 한 만큼 추가.
        real_income =  real_income + rest_money * 0.85
    else:
        # 실 소득 : 3000 * 0.85 한 만큼 추가.  남은 돈 추가 정산.
        real_income =  real_income + 3000 * 0.85
        rest_money = rest_money - 3000
        
        # 남은돈이 4천 이하? 아닌가?
        if rest_money <= 4000:
            # 남은돈 전부 24% 징수
            real_income =  real_income + rest_money * 0.76
        else:
            # 4000은 24% 징수, 그러고도 남은 돈은 35% 징수.
            real_income =  real_income +  4000 * 0.76
            rest_money = rest_money - 4000
            
            real_income = real_income + rest_money * 0.65

    
print(f'실 소득 금액 : {real_income}')