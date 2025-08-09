#다익스트라 백준 1753
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,E = map(int,input().split())
S = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))

dist = [sys.maxsize] * (V+1)
visited = set()

dist[S] = 0
q = PriorityQueue()
q.put((0,S))

while q.qsize() > 0:
  node = q.get()[1]
  if node in visited:
    continue

  visited.add(node)

  for adj in graph[node]:
    next = adj[0]
    weight = adj[1]
    if dist[next] > dist[node] + weight:
      dist[next] = dist[node] + weight
      q.put((dist[next],next))

for i in range(1, V+1):
  if i in visited:
    print(dist[i])
  else:
    print('INF')
