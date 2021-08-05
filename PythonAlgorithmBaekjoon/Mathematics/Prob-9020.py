import sys
import math

testCase = int(sys.stdin.readline())

#에라토스체로 소수 리스트 구하기 math.sqrt()의 값보다 항상 이하기때문
def deci(number):

    deciList = [True]*number
    era = int(math.sqrt(number))+1
    for i in range(2, era):
        if deciList[i] == True:
            for j in range(i+i, number, i):
                deciList[j] = False
    return [i for i in range(2, number) if deciList[i] == True]

#최댓값의 중앙이하의 최대 인덱스를 기준으로 낮춰가면서 최댓값찾기!
def findAns(number):
    deciList = deci(number)
    idx = max([i for i in range(len(deciList)) if deciList[i] <= number/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(deciList)):
            if deciList[i]+deciList[j] == number:
                return deciList[i], deciList[j]

for i in range(testCase):
    case = int(sys.stdin.readline())
    smaller, bigger = findAns(case)
    print(smaller, bigger)
