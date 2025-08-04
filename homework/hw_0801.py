# 7. 위에서 생성한 데이터 프레임을 활용하여 
# 2016년부터 2024년까지 연도별 영치대수 선 그래프를 matplotlib을 이용해 그리십시오.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'.\대구광역시 동구_연도별 체납차량 번호판 영치실적_20241201.csv')

data1 = pd.DataFrame(data,columns=['년도','영치대수','체납건수','체납금액(백만원)'])
data1.sort_values(by='년도',inplace=True)
x = data1['년도']
y = data1['영치대수']
plt.plot(x,y,color='red')
plt.title('monetary penalty by year')
plt.xlabel('year')
plt.ylabel('money')
plt.show()