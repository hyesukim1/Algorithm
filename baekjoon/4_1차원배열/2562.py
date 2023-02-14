# 최댓값

a = []

for i in range(0, 9):
    n = int(input())
    a.append(n)
print(max(a))
b = a.index(max(a))
print(b+1)