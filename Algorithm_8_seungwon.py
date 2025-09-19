## 백준 1931번
from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

N = int(input())

pq = PriorityQueue()

for _ in range(N):
  [s,f] = list(map(int, input().split()))
  pq.put((f,[s,f]))

S = []
S.append(pq.get()[1])

for _ in range(N-1):
  meet = pq.get()
  if S[-1][1] <= meet[1][0]:
    S.append(meet[1])

print(len(S))



## DP version

N = int(input())
mt = [tuple(map(int, input().split())) for _ in range(N)]
mt.sort(key=lambda x: x[1])

dp = [0] * (N + 1)

for i in range(1, N + 1):
    s, f = mt[i - 1]
    j = 0
    for k in range(i - 1, 0, -1):
        if mt[k - 1][1] <= s:
            j = k
            break
    dp[i] = max(dp[i - 1], dp[j] + 1)

print(dp[N])