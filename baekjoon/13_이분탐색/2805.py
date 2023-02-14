# 나무자르기

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
start, end = 0, max(tree)
ans = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in tree:
        if i >= mid:
            cnt += i - mid
            if cnt > M:
                break
    if cnt >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)