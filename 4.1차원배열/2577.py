# 숫자의 개수
'''
# 내가 푼거=형편없.,,
a = []

for i in range(0, 3):
    n = int(input())
    a.append(n)
    
b = a[0]*a[1]*a[2]
x = [int(c) for c in str(b)]
print(x)

for j in range(0, 9):
'''

# 구글링
a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))