import sys
#해당 행과 열을 받아와 그 지점부터 8*8의 체스판을 검사하는 함수
#반환값은 기존의 W와 B로 시작하는 각각의 패턴과 값이 다른 개수이다.
def checkPattern(box,row,col):
    #B로 시작하는 / W로 시작하는 정답 체스팝
    global rightPanelB, rightPanelW
    #반환값
    faultA = 0
    faultB = 0
    patternIdx = 0

    #시작이 W인 경우
    for rowLine in range(row,row+8):
        for colLine in range(col,col+8): 
            if rightPanelW[patternIdx] != box[rowLine][colLine]:
                faultA+=1
            patternIdx+=1
    #시작이 B인 경우
    patternIdx = 0
    for rowLine in range(row,row+8):
        for colLine in range(col,col+8): 
            if rightPanelB[patternIdx] != box[rowLine][colLine]:
                faultB+=1
            patternIdx+=1
    #파이썬식 삼항연산
    return faultA if faultA < faultB else faultB

patternChW = ['W','B'] *4 #W로 시작하는 열
patternChB = ['B','W'] *4 #B로 시작하는 열

rightPanelW = (patternChW + patternChB) * 4 #W - 체스판
rightPanelB = (patternChB + patternChW) * 4 #B - 체스판

M, N = map(int,sys.stdin.readline().split())
chessPanel = ["" for i in range(M)]

for i in range(M):
    #map형식을 읽기로 사용하기 위해서는 리스트로 변환 필요
    chessPanel[i] = list(map(str,sys.stdin.readline()))
    chessPanel[i].remove('\n')

minFalult = 64

for i in range(M-7):
    for j in range(N-7):
      if minFalult > checkPattern(chessPanel,i,j):
          minFalult = checkPattern(chessPanel,i,j)

#최솟값 출력
print(minFalult)
