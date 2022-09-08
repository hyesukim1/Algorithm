# 킹

chess = [1, 1, 2, 2, 2, 8]
number = list(map(int, input().split()))

for i in range(6):
    ans = chess[i] - number[i]
    print(ans)

