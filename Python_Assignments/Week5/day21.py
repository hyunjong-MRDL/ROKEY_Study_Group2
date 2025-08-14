import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

sns.histplot(data=data)
# Python matplotlib에서 LaTeX 사용하는 방법
## raw-text (r"") 내부에서 $로 감싼 부분은 LaTeX로 인식
plt.title(r"Normal distribution ($\mu=50, \sigma=10$)")
plt.show()