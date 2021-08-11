import sys

#6 - 5666
#7 - 6666이 아니다.
#7의 경우 7번째로 666이 들어가는 숫자를 말하므로 6660이 되는 것이다.

N = int(sys.stdin.readline())
deadSig = 666
count = 0

while True:
    if '666' in str(deadSig):
        count+=1
        if count == N : 
            print(deadSig)
            break
    deadSig+=1

# 틀렸던 코드 
# import sys

# N = int(sys.stdin.readline())
# deadSig = '666'
# count = 0

# for i in range(10000):
#     if deadSig in str(i):
#         count +=1
#     if count == N:
#         print(i)
#         break