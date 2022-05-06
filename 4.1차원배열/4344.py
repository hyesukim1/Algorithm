# 내일 다시 풀기
# 평균은 넘겠지
n = int(input())

for i in range(n):
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:])/score_list[0]
    cnt = 0
    for j in score_list[1:]:
        if j > avg:
            cnt+=1
    rate = cnt/score_list[0] * 100
    print(f'{rate:.3f}%')