##백준11399번

# import sys
# input = sys.stdin.readline
from collections import deque

N = int(input())
P_list = list(map(int,input().split()))
P_s = deque(sorted(P_list))

S = 0
T = 0

for i in range(N):
  p = P_s.popleft()
  T += p
  S += T

print(S)


##백준 1744번

# import sys
# input = sys.stdin.readline
from collections import deque

N = int(input())

plus = []
minus = []
one = []
zero = []

for i in range(N):
  num = int(input())

  if num >= 2 :
    plus.append(num)
  elif num < 0:
    minus.append(num)
  elif num == 1:
    one.append(num)
  elif num == 0:
    zero.append(num)

S = 0

plus = deque(sorted(plus))
while len(plus) > 1:
  m = plus.pop()
  n = plus.pop()
  S += m*n
if len(plus) == 1:
  S += plus.pop()

minus = deque(sorted(minus))
while len(minus) > 1:
  p = minus.popleft()
  q = minus.popleft()
  S += p*q
if len(minus) == 1:
  if len(zero) != 0:
    S += (minus.popleft() * zero.pop())
  elif len(zero) == 0:
    S += minus.popleft()

while len(one) != 0:
  r = one.pop()
  S += r

print(S)