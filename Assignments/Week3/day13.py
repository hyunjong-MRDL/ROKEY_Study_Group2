# 예외 처리
numerator = 10
denominator = [1, 2, 3, 0, 5, 6, 7, 0, 9]
for d in denominator:
    try:
        print(numerator / d)
    except ZeroDivisionError: # 예외 발생 시 실행되는 부분 (예외 처리 안하면 프로그램 중단)
        print("0으로 나눌 수 없습니다!")