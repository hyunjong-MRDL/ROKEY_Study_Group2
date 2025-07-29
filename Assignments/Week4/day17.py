binary_map = [[0,1,1,1,1,1],
              [0,1,0,0,0,1],
              [0,1,0,1,0,1],
              [0,1,0,1,0,0],
              [0,0,0,1,1,0],
              [1,1,1,1,1,0]]

rows = len(binary_map)
cols = len(binary_map[0])

            #  down    up    right   left
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(i, j):
    queue = [(i, j)]
    visited = [(i, j)]

    while queue:
        ci, cj = queue.pop(0)
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            # map 범위 내에서 \ 갈 수 있고, 가지 않은 길
            if (0 <= ni < rows and 0 <= nj < cols) \
            and (binary_map[ni][nj] == 0 and (ni, nj) not in visited):
                visited.append((ni, nj))
                queue.append((ni, nj))
    
    return visited

route = bfs(0,0)

for i in range(0, len(route), 5):
    chunk = route[i:i+5]
    print(" ".join(map(str, chunk)))