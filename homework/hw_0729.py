# grid = [
#     [0, 1, 1, 1, 1, 1],
#     [0, 1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1, 0],]
# n = len(grid)       # 행 개수
# m = len(grid[0])    # 열 개수
# visited = [[False] * m for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs_stack(start_x, start_y):
#     for i in range(n):
#         for j in range(m):
#             visited[i][j] = False
#     stack = [(start_x, start_y)]
#     while stack:
#         x, y = stack.pop()
#         if x < 0 or x >= n or y < 0 or y >= m:
#             continue
#         if grid[x][y] == 1 or visited[x][y]:
#             continue
#         visited[x][y] = True
#         print(f"방문: ({x}, {y})")
#         for direction in range(4):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             stack.append((nx, ny))
# dfs_stack(0, 0)

# rows, cols = map(int, input("행(세로)과 열(가로)을 입력하세요: ").split())
# grid = []
# for i in range(rows):
#     row_data = list(map(int,input(f"{i+1}번째 행 데이터를 {cols}개 입력하세요 (0 혹은 1): ").split()))
#     grid.append(row_data)
# print("생성된 2차원 리스트(지도)입니다:")
# for i in grid :
#     print(i)

grid = [ [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],]
n = len(grid)       # 행 개수
m = len(grid[0])    # 열 개수
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs_list(start_x, start_y):
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    queue = [(start_x, start_y)]
    visited[start_x][start_y] = True
    while queue:
        x, y = queue.pop(0)
        print(f"방문: ({x}, {y})")
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grid[nx][ny] == 1 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
