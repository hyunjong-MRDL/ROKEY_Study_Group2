# https://www.acmicpc.net/problem/5597
# 
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 
# 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 
# 1번부터 30번까지 출석번호가 붙어 있다. -> 기존 데이터 30번째

# 교수님이 내준 특별과제를 28명이 제출했는데, 
# 그 중에서 제출 안 한 학생 2명의 출석번호를 
# 구하는 프로그램을 작성하시오.

# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 
# 1차 조건: n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. -> 입력이 하나씩 총 28번일어나고 범위는 1<= n  <=30
# 2차 조건 : 입력자체 출석번호에 중복은 없다. -> 중복 없이 너가 알아서 입력해라.

# 출력
# 출력은 2줄이다. 
# 3차 조건 : 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 
# 2번째 줄에선 그 다음 출석번호를 출력한다. -> 올림차순 앞 > 뒤 


student_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
        18,19,20,21,22,23,24,25,26,27,28,29,30]
enterlist_fin = []
enter = []

while len(enterlist_fin) != 28: #0~27까지 총 28번
    num = int(input(''))

#1차 조건 
    if 1<= num and num <=30 : 
        enterlist_fin.append(num)
        enterlist_fin= list(set(enterlist_fin))



    else :
        continue

#3차 조건
enterlist_fin = set(student_num) - set(enterlist_fin)
enterlist_fin = list(enterlist_fin)

for i in enterlist_fin:
    print(i)



student = [i for i in range(1,31)] #1~30번 출석번호
# -> [1,~ 30]

for _ in range(28):
    num = int(input())
    student.remove(num)
    
for i in student:
    print(i)