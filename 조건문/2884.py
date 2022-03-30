H, M = map(int, input().split())

if M > 44:
    print(H, M-45)
elif M < 45 and H > 0:
    print(H-1, M+15)
else:
    print(23, M+15)
    
'''
해설
> H(시간), M(분)에 맵 함수를 띄어쓰기로 받기

> M이 45분 보다 클때 M-45분해줌
M이 45분보다 작고 H이 0보다 클때 15분을 더해줘야함

> H가 0시(=12시)이면 print(23)으로 출력
'''
        