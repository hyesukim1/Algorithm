a, b, c = map(int, input().split())

sum1 = (a+b)%c
sum2 = ((a%c)+(b%c))%c
mul1 = (a*b)%c
mul2 = ((a%c)*(b%c))%c

print(sum1)
print(sum2)
print(mul1)
print(mul2)
