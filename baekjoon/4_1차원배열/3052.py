# 나머지
num = []

for i in range(10):
    n = int(input())
    a = n%42
    num.append(a)
    
num = set(num) # set함수는 중복을 없애줌
print(len(num))
