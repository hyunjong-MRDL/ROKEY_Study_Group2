n = int(input())

# 회의 정보를 담을 리스트
array = []
for _ in range(n):
  # 시작 시간, 끝나는 시간, 회의 인원 입력
  array.append(list(map(int, input().split())))

# 시작 시간 기준 오름차순 정렬
array.sort()

dp = [0] * n
dp[0] = array[0][2]
for i in range(1, n):
  dp[i] = max(dp[i - 1], dp[i - 2] + array[i][2])

print(dp[n - 1])