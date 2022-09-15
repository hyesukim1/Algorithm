# 수 정렬하기

n = int(input())
ans = []

for i in range(n):
    ans.append(int(input()))

answer = sorted(ans)

for i in range(len(answer)):
    print(answer[i])