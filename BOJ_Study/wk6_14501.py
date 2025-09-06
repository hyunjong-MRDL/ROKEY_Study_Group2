"""
14501: 퇴사

퇴사까지 남은 N일 동안 최대한 많은 상담 비용 수집
하루 1회, 매일 다른 사람과 상담
상담 기간 T, 상담 비용 P
"""

# 문제 데이터 입력받기
N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

# ========= 풀이 1: Brute-Force =========
def find_max_profit(curr_day: int, total_price: int):
    global maximum

    # 종료 조건 (퇴사일 도달)
    if curr_day >= N:
        maximum = max(maximum, total_price)

    # 아직 상담을 더 진행할 수 있는 경우
    else:
        # 상담 진행 선택 (퇴사 전에 완료 가능할 때)
        if curr_day + T[curr_day] <= N:
            find_max_profit(curr_day + T[curr_day], total_price + P[curr_day])
        # 상담 건너 뛰기 (언제나 가능)
        find_max_profit(curr_day + 1, total_price)

maximum = 0
find_max_profit(0, 0)

print(maximum)

# ============= 풀이 2: DP =============

dp = [0] * (N+1)
for day in range(N-1, -1, -1):
    # 아래 두 가지 중 최대값 선택

    # (1) 현재 날짜(day)에 상담이 완료 가능한 경우
    consult = 0
    if day + T[day] <= N:
        consult = dp[day+T[day]] + P[day]
    # (2) 상담 건너 뛰는 경우
    skip = dp[day+1]
    dp[day] = max(consult, skip)

print(dp[0])