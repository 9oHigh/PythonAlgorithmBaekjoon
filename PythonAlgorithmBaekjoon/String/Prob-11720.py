import sys

cnt = int(input())
newlist = list(input())
#예외처리
if cnt < len(newlist):
    sys.exit(0)
answer = 0

for i in newlist:
    answer += int(i)
print(answer)
