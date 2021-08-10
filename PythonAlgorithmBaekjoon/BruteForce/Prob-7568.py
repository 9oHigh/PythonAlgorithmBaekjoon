import sys

N = int(sys.stdin.readline())

myList = [[0,0] for i in range(N)]
rankList = [1 for i in range(N)]

#리스트[인덱스] = 리스트(Map(타입,입력))
for i in range(N):
    myList[i] = list(map(int,sys.stdin.readline().split()))

#키와 몸무게를 비교
for i in range(N):
    kg,height = myList[i]
    for j in range(N):
        if i == j: continue

        otherKg,otherHeight = myList[j]

        #두 개의 값이 모든 큰 경우 -> 랭크는 하락
        if kg < otherKg and height < otherHeight:
            rankList[i]+=1

    print(rankList[i],end=" ")



