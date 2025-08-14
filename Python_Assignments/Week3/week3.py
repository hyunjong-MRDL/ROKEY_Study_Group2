while True:
    name = input("이름을 입력하세요: ")
    try:
        age = int(input("나이를 입력하세요: "))
        if age < 0:
            print("나이를 정확히 입력해주세요.")
            continue
    except ValueError:
        print("나이에서 ValueError가 발생했습니다!")
        continue

    print(f"당신의 이름: {name}")
    print(f"당신의 나이: {age}")
    break