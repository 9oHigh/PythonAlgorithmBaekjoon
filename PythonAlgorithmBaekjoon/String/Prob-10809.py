from string import ascii_lowercase

newlist = []
anslist = []
alpha_list = list(ascii_lowercase)
newlist = input()

for i in alpha_list:
    count = 0
    for j in newlist:
        if i == j:
            anslist.append(str(newlist.index(j)))
            count += 1
            break
    if count > 0:
        continue
    else:
        anslist.append(str(-1))
#리스트 문자열 변환
print(' '.join(anslist))
