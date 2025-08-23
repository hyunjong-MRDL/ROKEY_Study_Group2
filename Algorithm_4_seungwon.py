##백준11404번:가장 빠른 버스 노선 구하기

import sys
#input = sys.stdin.readline

V = int(input())
E = int(input())

D = [[sys.maxsize for j in range(V+1)] for i in range(V+1)]
for i in range(V+1):
  D[i][i] = 0

for i in range(E):
  i,j,w = map(int,input().split())
  if D[i][j] > w:
    D[i][j] = w

for k in range(V+1):
  for i in range(V+1):
    for j in range(V+1):
      if D[i][j] > D[i][k] + D[k][j]:
        D[i][j] = D[i][k] + D[k][j]

for i in range(1,V+1):
  for j in range(1,V+1):
    if D[i][j] == sys.maxsize:
      print(0,end=' ')
    else:
      print(D[i][j],end=' ')
  print()