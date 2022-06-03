# 상수

n = input().split()

num = []

for i in n:
    b = i[::-1]
    num.append(b)
print(num)
    
if int(num[0]) > int(num[1]):
    print(num[0])
elif int(num[1]) > int(num[0]):
    print(num[1])
else:
    None