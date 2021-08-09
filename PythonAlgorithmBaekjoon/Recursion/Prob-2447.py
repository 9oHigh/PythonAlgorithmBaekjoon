import sys
#재귀함수
def drawStar(number):
    #전역변수 - 2차원 배열
    global Map
    #재귀탈출
    if number == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return 0

    point = number//3
    drawStar(number//3)
    for i in range(3):
        for j in range(3):
            #중간부분은 값변환x
            if i == 1 and j == 1:
                continue
            for k in range(point):
                #***
                #* *
                #*** 를 하나로 보고 3개 단위로 끊기
                Map[point*i+k][point*j:point*(j+1)] = Map[k][:point] 

N = int(sys.stdin.readline())      
#2차원 배열 Map
Map = [[0 for i in range(N)] for i in range(N)]

drawStar(N)
#1인부분만 *로 변환
for i in Map:
    for j in i:
        if j == 1:
            print('*',end = '')
        else:
            print(' ',end = '')
    print()