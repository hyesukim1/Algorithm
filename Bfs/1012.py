# 유기농 배추

test_case = int(input())
m, n, k = map(int, input().split(' '))
graph = [a for a in range(map(int, input()))]

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1: