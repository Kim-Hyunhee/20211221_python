product_price = int(input('총 구매 금액 : '))
mileage = int(input('마일리지 사용 금액 : '))
coupon = input('사용 : T / 미사용 : F : ')

if coupon == 'T':
    real_price = (product_price * 0.9) - mileage
else :
    real_price = product_price - mileage

if real_price >= 30000 :
    delivery = 0   
else : 
    delivery = 3500
     
real_price2 = int(real_price)
print(f'총 구매금액 : {product_price}원, 배송료 : {delivery}, 실 결제 금액 :{real_price2}')


total_product_price = int(input('총 구매 금액 입력 : '))
mileage = int(input('마일리지 사용 금액 : '))
use_coupon = input('쿠폰 사용 여부(T/F) : ')

# 실 결제 금액 변수 => 총 구매금액으로 초기화
real_price = total_product_price

# 쿠폰 사용? T면 실 결제금액 * 0.9 처리

if use_coupon == 'T' :
    real_price = real_price *0.9
    
# 마일리지 -> 실 결제금액 - 마일리지 금액처리 (0원이어도 -0이니 정상 작동)
real_price = real_price - mileage

# 배송비가 3500원이라고 우선 세팅
shipment_pay = 3500

# 실 결제금액이 3만원 이상? 배송비를 0원으로 변경
if real_price >= 30000 :
    shipment_pay = 0
    
# 결정된 배송비를 결제 금액에 추가
real_price = real_price + shipment_pay

# 정수로 변경
real_price = int(real_price)
result_str = f'총 구매금액 : {total_product_price}, 배송료 : {shipment_pay}, 실 결제 금액 : {real_price}'

print(result_str)