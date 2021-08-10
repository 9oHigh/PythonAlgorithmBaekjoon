import sys

N,M = map(int,sys.stdin.readline().split()) #카드의 개수, 최댓값
numbers = list(map(int,sys.stdin.readline().split())) #리스트로 입력

Max = 0

for i in numbers:
    for j in numbers:
        for k in numbers:
            #다른 수,가장 큰 값(가까운 값)
            if i!=j and j!=k and k!=i and i+j+k>Max and i+j+k<= M:
                Max = i+j+k

print(Max)