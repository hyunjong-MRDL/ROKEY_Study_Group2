from sys import stdin
SIZE = 9

sudoku_map = [list(map(int, stdin.readline().strip().split())) for _ in range(SIZE)]

# 빈 칸 탐색 및 리스트로 저장
blank_list = []
for i in range(SIZE):
    for j in range(SIZE):
        if sudoku_map[i][j] == 0:
            blank_list.append((i, j))

# 스도쿠 유효성 검사
def is_valid(row, col, num):
    # 행/열 단위 검사
    for i in range(SIZE):
        if sudoku_map[row][i] == num or sudoku_map[i][col] == num:
            return False
    
    # 셀(3x3) 단위 검사
    i_start, j_start = row // 3, col // 3
    for i in range(3 * i_start, 3 * i_start + 3):
        for j in range(3 * j_start, 3 * j_start + 3):
            if sudoku_map[i][j] == num:
                return False

    return True

# n: 채운 빈 칸의 개수
def solve(n):
    # 종료 조건: 모든 빈 칸을 채운 경우
    if n == len(blank_list):
        for row in sudoku_map:
            for num in row:
                print(num, end=" ")
            print()
        exit(0)
    
    # 각 빈 칸에 대해
    i, j = blank_list[n]
    # 스도쿠에 넣을 수 있는 모든 수(1~9)에 대해
    for num in range(1, 10):
        # 스도쿠 규칙을 만족하면
        if is_valid(i, j, num):
            sudoku_map[i][j] = num
            # 다음 빈 칸 탐색
            solve(n+1)
            # 직전의 시도가 틀린 경우, 이전 상태로 backtracking
            sudoku_map[i][j] = 0

solve(0)