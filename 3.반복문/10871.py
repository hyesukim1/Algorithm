# x보다 작은 수 

a, b = map(int, input().split())

A = list(map(int, input().split()))

for i in range(a):
    if A[i] < b:
        print(A[i], end=' ')