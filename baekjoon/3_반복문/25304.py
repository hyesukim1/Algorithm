# 영수증
import sys

total_price = int(input())
product_num = int(input())

check_price = []

for i in range(product_num):
    a, b = map(int, sys.stdin.readline().split())
    price =  a*b
    check_price.append(price)

ans = sum(check_price)

if ans == total_price:
    print('Yes')
else:
    print('No')