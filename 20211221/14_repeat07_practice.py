num = int(input('숫자 입력 : '))

for i in range(1, num+1) :
    if i % 3 == 0:
        print(i)

for i in range(1, num+1) :
    if i % 3 == 0:
        if i != 0:
            print(i)