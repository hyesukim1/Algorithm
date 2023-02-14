# 셀프 넘버

# 함수 d(n)
def d(n):
    # 생성자 n을 이용해 d(n)을 만드는 수식
    n = n + sum(map(int, str(n)))
    return n

# 셀프 넘버가 아닌 수(생성자가 있는 수)가 들어갈 집합
no_selfnum = set()

# no_selfnum 집합에 들어갈 수들을 찾아 넣기
for i in range(1, 10001):
    no_selfnum.add(d(i))

# 셀프 넘버 출력
for j in range(1, 10001):
    if j not in no_selfnum:
        print(j)