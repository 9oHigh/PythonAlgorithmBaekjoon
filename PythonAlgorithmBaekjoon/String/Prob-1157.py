words = input().upper()

# 입력받은 문자열에서 중복값을 제거
unique_words = list(set(words))

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    # count 숫자를 리스트에 append
    cnt_list.append(cnt) 

# count 숫자 최대값이 중복되면
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    # count 숫자 최대값 인덱스(위치)
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])