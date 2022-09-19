# 통계학

n = int(input())

list = []

for i in range(n):
    num = int(input())
    list.append(num)

# 평균
print(sum(list)/len(list))

# 중앙값

srt = list.sort()
idx = 0
median = 0

if len(list)%2 == 0:
    idx = len(list) // 2
    median = (list[idx-1] + list[idx])/2
else:
    idx = len(list) // 2 + 1
    median = list[idx]
    
print(median)

# 최빈값


# 범위


