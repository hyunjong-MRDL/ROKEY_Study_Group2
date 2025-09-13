"""
12865: 평범한 배낭

무게 제한 K인 배낭에
무게 Wi, 가치 Vi의 물건들을 담아 만들 수 있는 최대의 가치를 구하는 프로그램
"""

import sys
input = sys.stdin.readline

# N: 물품의 개수, K: 준서가 견딜 수 있는 무게
N, K = map(int, input().split())
weights = [0 for _ in range(N+1)]
values = [0 for _ in range(N+1)]
for i in range(1, N+1):
    weights[i], values[i] = map(int, input().split())

# DP[i][j]: i번째 물건까지 활용해서 무게 제한 j인 가방을 채우는 최대 가치
DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        # 현재 물건을 가방에 담을 수 있는 경우
        if j - weights[i] >= 0:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-weights[i]]+values[i])
        # 현재 물건을 담을 수 없는 경우 (무게 제한 초과)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][K])