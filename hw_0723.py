try :
    add = lambda x : x+9
    print(add(2))
    print(add(2)/0)
except ZeroDivisionError :
    print('0으로는 숫자를 나눌 수 없습니다.')