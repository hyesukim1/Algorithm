# 숫자카드 2

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
find = list(map(int, input().split()))

dic = {}

for i in card:
    if i in dic:
        dic[i] +=1
    else: 
        dic[i] =1

for i in find:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")