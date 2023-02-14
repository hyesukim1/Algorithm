# 미로탐색

from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우로 움직이도록 하는 lists
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # queue 초기화
    queue.append((x, y)) # 초기 위치
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4): # 4방향에 대해서 이동
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 밖으로 넘어간 경우
                continue
            if graph[nx][ny] == 0: # 이동할 수 없는 경우
                continue
            
            if graph[nx][ny] == 1: # nx,ny에 처음으로 이동했을 때
                graph[nx][ny] = graph[x][y] + 1 # graph[x][y]는 최소의 거리를 저장, 1을 더한 값을 graph[nx][ny]에 저장
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))