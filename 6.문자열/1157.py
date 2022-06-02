# 단어 공부
s = input().upper()
unique_s = list(set(s))

cnt = []
for x in unique_s:
    cnt_x = s.count(x)
    cnt.append(cnt_x)
    
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(unique_s[max_index])