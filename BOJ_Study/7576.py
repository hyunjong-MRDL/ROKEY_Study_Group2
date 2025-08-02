""" 7576번: 토마토 """
# 문제 링크: https://www.acmicpc.net/problem/7576
# 목적: N x M 창고에 있는 토마토가 다 익는 데 최소 며칠 걸리는지 찾기
# 시나리오: "익은 토마토"의 [상/하/좌/우]에서 보관된 "덜 익은 토마토"는 하루가 지나면 익는다.
# 예외(1): 창고에 토마토가 들어있지 않은 빈 칸은 "-1"이 저장되어 있다.
# 예외(2): 시간이 아무리 지나도 창고에 있는 모든 토마토가 익지 않는 경우는 "-1"을 출력한다.

""" 풀이 시작 """
from collections import deque

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

# 시작점 찾을 때 채워야 할 칸 갯수도 저장하기
## check_success()를 사용할 경우 while문을 돌 때마다 MxN의 탐색 필요
### 시작점 찾을 때 채워야할 칸수도 미리 찾아두면 for(N){for(M)} 반복문 1회만 실행
def box_summary():
    starting_points = deque([])
    unripe = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                starting_points.append((i, j, 0))
            elif box[i][j] == 0:
                unripe += 1
    return starting_points, unripe

directions = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs():
    queue, to_fill = box_summary()

    while queue:
        if to_fill == 0:
            return queue.pop()[2]

        i, j, day = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
                queue.append((ni, nj, day+1))
                box[ni][nj] = 1
                to_fill -= 1

    return -1

print(bfs())