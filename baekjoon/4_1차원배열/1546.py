# 너무 어려움, 다시 풀어봐야할 듯

n = int(input())
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for i in test_list:
    new_score = i/max_score*100
    new_list.append(new_score)
test_avg = sum(new_list)/n
print(test_avg)

