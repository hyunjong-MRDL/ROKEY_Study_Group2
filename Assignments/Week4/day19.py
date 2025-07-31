import pandas as pd

df = pd.read_csv("data.csv")

total_stats = df.describe()

for category in total_stats.columns:
    stats = total_stats[category]
    print(f"{category} 평균: {stats["mean"]}, ", end="")
    print(f"최댓값: {int(stats["max"])}, 최솟값: {int(stats["min"])}")