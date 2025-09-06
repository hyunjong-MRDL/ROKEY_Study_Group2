#다익스트라 백준 1753
import heapq
import sys
input = sys.stdin.readline

# 1. 입력 및 초기화
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = sys.maxsize
distance = [INF] * (V + 1)

# 2. 간선 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 3. 다익스트라
def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))

# 4. 실행 및 출력
dijkstra(K)
for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
