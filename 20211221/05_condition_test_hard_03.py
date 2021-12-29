height = float(input('키 입력(cm 단위) : '))
weight = float(input('몸무게 입력(kg 단위) : '))

bmi = weight / ((height*0.01)*(height*0.01))
# bmi = weight / (height/100) / (height/100)


if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
elif bmi < 30:
    print('비만')
else :
    print('고도비만')