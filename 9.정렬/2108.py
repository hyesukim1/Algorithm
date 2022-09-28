from collections import Counter
# 통계학

n = int(input())

list = []

for i in range(n):
    num = int(input())
    list.append(num)

list.sort()
# print(list)

# s평균
print(round(sum(list)/len(list)))

# 중앙값
print(list[len(list) // 2])


# 최빈값
cnt = Counter(list).most_common(2)

if len(list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
            
# 범위
print((max(list)-min(list)))


