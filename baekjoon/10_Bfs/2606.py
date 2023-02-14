# 바이러스

from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    # 네트워크 연결
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v):
    q = deque([v])
    cnt = 0
    while q:
        pop = q.popleft()
        visited[pop] = True
        
        for i in graph[pop]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                cnt +=1
    print(cnt)

bfs(graph, 1)