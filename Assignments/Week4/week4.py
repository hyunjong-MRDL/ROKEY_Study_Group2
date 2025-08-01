import pandas as pd
import matplotlib.pyplot as plt

filename = r"대구광역시_체납차량_영치실적.csv"
df = pd.read_csv(filename, encoding='euc-kr')
# EUC-KR: Extended Unix Code - Korea
## 한글을 표현하기 위한 2 byte 문자 인코딩 방식
### 확장 버전: CP949

# Pandas 모듈의 기본 인코딩 방식: UTF-8
## UTF: Unicode Transformation Format (8-bit)

# 인코딩 방식(1)로 저장된 파일을 인코딩 방식(2)로 불러오려고 하면 오류 발생

years = df["년도"].tolist()
confiscated = df["영치대수"].tolist()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title("대구광역시 연도별 영치대수")
plt.plot(years, confiscated)
plt.xlabel("년도")
plt.ylabel("차량 대수")
plt.grid()
plt.show()