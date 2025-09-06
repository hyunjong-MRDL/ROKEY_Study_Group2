from sys import stdin

""" 11726: 2*n 타일링 II """
N_rect = int(stdin.readline())   # 직사각형의 크기

if N_rect == 1:
    print(1)
else:
    # DP 배열 초기화
    num_cases = [0] * (N_rect+1)
    num_cases[1] = 1
    num_cases[2] = 3

    # DP 배열 채우기
    for i in range(3, N_rect+1):
        num_cases[i] = (num_cases[i-1] + 2*num_cases[i-2]) % 10007
    
    print(num_cases[N_rect])

# ============ 문제 분리선 ============
""" 1932: 정수 삼각형 """
N = int(stdin.readline())  # 삼각형의 크기

# 정수 삼각형 입력받기
triangle = []
for i in range(N):
    line = list(map(int, stdin.readline().split()))
    line.extend([-1] * (N - (i+1)))
    triangle.append(line)

# DP 배열 초기화
dp = [[None] * N for _ in range(N)]
dp[0][0] = triangle[0][0]

# DP 배열 채우기
for i in range(1, N):
    for j in range(N):
        if triangle[i][j] != -1:
            # dp[i][j] 값을 계산
            # (1) 왼쪽 위 [i-1, j-1]
            # (2) 바로 위 [i-1, j]
            left_up, just_up = 0, 0
            if 0 <= i-1 < N and 0 <= j-1 < N and dp[i-1][j-1] is not None:
                left_up = dp[i-1][j-1]
            if 0 <= i-1 < N and 0 <= j < N and dp[i-1][j] is not None:
                just_up = dp[i-1][j]
            dp[i][j] = max(left_up+triangle[i][j], just_up+triangle[i][j])

print(max(dp[N-1]))