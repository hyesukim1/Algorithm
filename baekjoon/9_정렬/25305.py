# 커트라인

num, win = map(int, input().split())
n = list(map(int, input().split()))
# print(n)

n.sort(reverse=True)
print(n[win-1])