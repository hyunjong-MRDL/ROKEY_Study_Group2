import requests
import json

# url = 'https://randomuser.me/api/'
    
# response = requests.get(url)
# data = json.loads(response.text)

# user_info = data['results'][0]['name']
# title = user_info['title']
# first = user_info['first']
# last = user_info['last']
    
# full_name = f'{title} {first} {last}'
# print('랜덤 사용자 이름:', full_name)

#9번문제

# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# font_path = 'C:/Windows/Fonts/malgun.ttf'
# font_name = fm.FontProperties(fname=font_path).get_name()
# plt.rc('font', family=font_name)
# fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
# sales = [150, 200, 125, 90, 175]
# fig, ax = plt.subplots(figsize=(8, 6))
# bars = ax.bar(
#     fruits,
#     sales,
#     color=['#FF9999', '#FFE699', '#FFCC99', '#CC99FF', '#FF99CC'],
#     edgecolor='gray'
# )

# ax.set_title('과일별 판매량', fontsize=16)
# ax.set_xlabel('과일 종류', fontsize=12)
# ax.set_ylabel('판매량 (개)', fontsize=12)
# ax.set_ylim(0, max(sales) + 50)

# plt.tight_layout()
# plt.show()


#10번 문제
import re
# YYYY-MM-DD 형태의 날짜만 캡처
pattern = re.compile("\d{4}-\d{2}-\d{2}")
input_path = r"sample_folder\logfile.log"
with open(input_path,'w',encoding='utf-8') as file:
    file.write("2025-03-30 12:00:01 INFO 서버 시작됨\n")
    file.write("2025-03-30 12:05:12 ERROR 데이터베이스 연결 실패\n")
    file.write("2025-03-30 12:10:35 WARNING 응답 속도 저하\n")
    file.write("2025-03-30 12:15:45 ERROR 사용자 인증 실패\n")

with open(input_path, "r", encoding="utf-8") as infile:
    for line in infile:
        match = pattern.match(line)
        print(match)
