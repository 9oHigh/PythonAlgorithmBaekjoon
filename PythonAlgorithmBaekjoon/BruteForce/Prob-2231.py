import sys

#각각의 자리값과 자기자신을 더한 값을
#반환하는 함수
def sumPosi(num):
    result = num
    while num > 0 :
        if num < 10:
            result+= num
            break
        else:
            result += (num%10)
            num//=10

    return result

N = int(sys.stdin.readline())
noneResult = 0
#입력받은 값과 더한 값 비교 후 출력
for i in range(N):
    if N == sumPosi(i):
        noneResult+=1
        print(i)
        break

if noneResult == 0: print(noneResult)
