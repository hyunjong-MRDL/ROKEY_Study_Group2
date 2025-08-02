###백준 7562번 문제(나이트의 이동)
from collections import deque

def bfs(c_board, start, goal):
    # 전달 인수 c_board는 체스판의 한변의 길이(칸 개수), start는 탐색 시작 좌표, goal은 최단경로(이동횟수)를 구할 목표 좌표
    x, y = start

    queue = deque() #queue 생성
    queue.append((x, y, 0))  # (현재 좌표 x, y, 이동한 횟수)->시작좌표를 추가해줌
    visited = set()          # 방문한 좌표 집합

    while queue:
        x, y, l = queue.popleft()  # 현재 좌표와 이동 횟수

        # 이미 방문한 경우 skip(while문 처음으로 돌아가 다른 좌표를 pop해온다)
        if (x, y) in visited:
            continue

        # 방문 표시
        visited.add((x, y))

        # 목표 좌표에 도착한 경우 이동 횟수 반환
        if (x, y) == goal:
            return l

        # 나이트가 이동할 수 있는 방향들
        directions = [(-2,1), (-2,-1), (-1,-2), (1,-2), (2,1), (2,-1), (-1,2), (1,2)]

        #인접 노드들을 리스트에 추가(즉, 나이트가 갈 수 있는 경로들의 좌표를 추가)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 유효한 좌표 범위 내이고 아직 방문하지 않았다면 큐에 추가
            if 0 <= nx < c_board and 0 <= ny < c_board and (nx, ny) not in visited:
                queue.append((nx, ny, l + 1))

# 테스트 케이스 입력 및 출력
print('--입력--')
test_num = int(input())
ans = []
for _ in range(test_num):
    c_board = int(input())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    ans.append(bfs(c_board, start, goal))

print('--출력--')
for i in ans:
  print(i)


#경로를 출력
from collections import deque

def bfs_path(c_board, start, goal):
    x, y = start

    queue = deque()
    queue.append([(x,y)]) #queue에 좌표대신 좌표들의 시퀀스인 리스트 즉, path들을 담아줌. 초기값으로는 start좌표만 담긴 path를 추가해준다.
    visited = set()

    while queue:
        path = queue.popleft()  #queue에서 좌표대신 경로를 뽑음

        x, y = path[-1] #visited를 판별할 현재 좌표 x,y는 가져온 path의 맨 마지막 좌표인 path[-1]

        if (x, y) in visited:
            continue


        visited.add((x, y))


        if (x, y) == goal:
            return  path  #최단경로를 반환

        directions = [(-2,1), (-2,-1), (-1,-2), (1,-2), (2,1), (2,-1), (-1,2), (1,2)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < c_board and 0 <= ny < c_board and (nx, ny) not in visited:
                new_path = path + [(nx, ny)]  #기존 경로 path에 새로운 좌표 (nx,ny)가 추가된 새로운 경로 new_path
                queue.append(new_path)  #새로운 경로인 new_path를 queue에 추가해줌.


#테스트 케이스 입력 및 출력
print('--입력--')
test_num = int(input())
ans = []
for _ in range(test_num):
    c_board = int(input())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    ans.append(bfs_path(c_board, start, goal))

print('--출력--')
for i in ans:
  print(i)