textfile = "C:/rokey/python/ch12/pizza_file1.txt"

# write mode : 새로운 내용을 작성하고 파일에 덮어쓰기
with open(textfile, "w", encoding="utf-8") as f:
    f.write("페퍼로니피자 3000\n치즈피자 3200\n콤비네이션피자 3500\n")

# append mode : 새로운 내용을 작성하고 파일에 추가하기
with open(textfile, "a", encoding="utf-8") as f:
    f.write("불고기피자 3600\n해산물피자 3800\n")

pizzas = []
# read mode : 파일에 작성된 내용을 읽어오기
with open(textfile, "r", encoding="utf-8") as f:
    lines = f.readlines() # 개행 문자 (\n) 기준으로 잘라서 List로 반환
    for l in lines:
        name, price = l.strip().split()
        pizzas.append(name)

print(pizzas)