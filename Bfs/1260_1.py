from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        # queue에서 맨 왼쪽의 값을 빼서 v로 지정
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, node+1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1
                
                
def dfs(v):
    visited2[v] = 1
    print(v, end=" ")
    for i in range(1, node+1):
        if visited2[i] == 0 and graph[v][i] == 1:
            dfs(i)

node, edge, start = map(int, read().split())
graph = [[0]*(node+1) for _ in range(node+1)]
visited = [0] * (node+1)
visited2 = [0] * (node+1)

for _ in range(edge):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

dfs(start)
print()
bfs(start)