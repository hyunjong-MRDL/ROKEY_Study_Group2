##백준 11657번 타임머신

import sys
#input = sys.stdin.readline

V,E = map(int,input().split())

edges = []
for _ in range(E):
  s,e,w = map(int,input().split())
  edges.append((s,e,w))

D = [sys.maxsize] * (V+1)
D[1] = 0

for i in range(V-1):
  for s,e,w in edges:
    if (D[s] != sys.maxsize) and (D[s] + w < D[e]):
      D[e] = D[s] + w

Neg_Cycle = False

for s,e,w in edges:
  if (D[s] != sys.maxsize) and (D[s] + w < D[e]):
      D[e] = D[s] +w
      Neg_Cycle = True


if not Neg_Cycle:
  for i in range(2,V+1):
    if D[i] != sys.maxsize:
      print(D[i])
    else:
      print(-1)
else:
  print(-1)

