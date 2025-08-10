""" 11729번: 하노이 탑 이동 순서 """
# 문제 링크: https://www.acmicpc.net/problem/11729
# 목적: 막대 'A'에 쌓여 있는 원판을 그 형태를 유지하면서 막대 'C'로 옮기기
# 조건 1: 한 번에 하나의 원판만 이동 가능
# 조건 2: 어떤 원판 위에 그보다 더 큰 원판을 쌓을 수 없다

""" 풀이 시작 """
from sys import stdin

def hanoi(N, start, via, end):
	# Start 막대에 원판이 1개만 남은 경우
    if N==1:
        print(start, end)
    
    # Start 막대에 원판이 2개 이상 남아있는 경우
    else:
		# Start 막대의 가장 아래에 있는 가장 큰 원판을 옮기기 위해 그 위에 있는 장애물 (N-1)개를 경유 지점 (via)로 치워둔다
        hanoi(N-1, start, end, via)
        # 위에 있던 장애물이 없어진 가장 큰 원판을 목적지 (end)로 이동한다
        hanoi(1, start, via, end)
        # 가장 큰 원판을 옮기기 위해 치워뒀던 나머지 원판을 마저 원래 목적지로 이동한다
        hanoi(N-1, via, start, end)

N = int(stdin.readline().strip())

# 최단 이동 횟수
min_moves = 2**N-1

hanoi(N, 1,2,3)

""" 예시 """
# hanoi(3, 1,2,3)
# ==== 재귀 호출 ====
	# [1] hanoi(2, 1,3,2)
#   ==== 재귀 호출 ====
		# [1.1] hanoi(1, 1,2,3)
		# [1.2] hanoi(1, 1,3,2)
		# [1.3] hanoi(1, 3,1,2)
    # [2] hanoi(1, 1,2,3)
	# [3] hanoi(2, 2,1,3)
#   ==== 재귀 호출 ====
		# [3.1] hanoi(1, 2,3,1)
		# [3.2] hanoi(1, 2,1,3)
		# [3.3] hanoi(1, 1,2,3)