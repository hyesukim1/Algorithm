# 수 정렬하기

''' 메모리 초과 ==> sorted 메모리 초과함
n =  int(input())
ans = []

for i in range(n):
    ans.append(int(input()))
    
answer = sorted(ans)

for j in range(len(answer)):
    print(answer[j])
'''

import sys

n = int(sys.stdin.readline())
inp = [0] * 10001

for i in range(n):
    nums = int(sys.stdin.readline())
    inp[nums] += 1


for j in range(10001):
    if inp[j] !=0:
        for k in range(inp[j]):
            print(j)