# 이분탐색의 탐색 종료 조건은 mid 값이 찾으려는 수랑 같으면 return을 해주고
# 찾는 값이 없을 떄 left가 right보다 커질 경우 종료

n = int(input())
n_list = list(map(int, input().split(' ')))
n_list.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

for num in targets:
    left, right = 0, n-1
    isExist = False

    while left <= right: # left가 right보다 작으면 루프를 돌림
        mid = (left + right) // 2
        if n_list[mid] == num:
            isExist = True
            print(1)
            break
        elif num < n_list[mid]:
            right = mid-1
        else:
            left = mid+1
    if not isExist:
        print(0)