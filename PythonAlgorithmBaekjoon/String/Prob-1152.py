words = input()
count = 1  # 문자열의 양끝이 모두 존재가정

for x in words:
    if x == ' ':
        count += 1

if words[0] == ' ':
    count -= 1
if words[-1] == ' ':
    count -= 1

print(count)
