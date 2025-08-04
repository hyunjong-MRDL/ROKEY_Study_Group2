def PB(num):
    de = []
    for i in num:
        if i in ('+','-','*','/'):
            b = de.pop()
            a = de.pop()
            
            if i == '+':
                result = a + b
            elif i == '-':
                result = a - b
            elif i == '*':
                    result = a * b
            elif i == '/':
                    result = a / b
            de.append(result)
        else :
            de.append(int(i))
    return de.pop()
a = input('후위 표기법 입력하시오 =')
num = a.strip().split(' ')
answer = PB(num)
print(answer)

