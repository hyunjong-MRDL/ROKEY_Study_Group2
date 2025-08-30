#백준 10844번 전체 코드
# import sys
# sys.stdin.readline

N = int(input())
D=[[0 for j in range(10)] for i in range(N+1)]

for j in range(1,10):
  D[1][j] = 1

for i in range(2,N+1):
  D[i][0] = D[i-1][1]
  D[i][9] = D[i-1][8]
  for j in range(1,9):
    D[i][j] = D[i-1][j-1] + D[i-1][j+1]

sum = 0

for j in range(10):
  sum = sum + D[N][j]

sum %= 1000000000

print(sum)




#백준 1149번 전체 코드
# import sys
# sys.stdin.readline

N = int(input())
Cost = [None]*(N+1)

for i in range(1, N+1):
 r,g,b = map(int,input().split())
 Cost[i] = [r,g,b]

DP = [[None]*3 for _ in range(N+1)]

for c in range(3):
  DP[1][c] = Cost[1][c]

for i in range(2,N+1):
  DP[i][0] = min(DP[i-1][1],DP[i-1][2]) + Cost[i][0]
  DP[i][1] = min(DP[i-1][0],DP[i-1][2]) + Cost[i][1]
  DP[i][2] = min(DP[i-1][0],DP[i-1][1]) + Cost[i][2]

print(min(DP[N]))