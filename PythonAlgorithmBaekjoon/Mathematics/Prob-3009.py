xSpotList = []
ySpotList = []
xPoint,yPoint = 0,0

for i in range(3):
    x,y = map(int,input().split())
    xSpotList.append(x)
    ySpotList.append(y)

for i in range(3):
    if xSpotList.count(xSpotList[i]) < 2:
        xPoint = xSpotList[i]
    if ySpotList.count(ySpotList[i]) < 2:
        yPoint = ySpotList[i]

print(xPoint,yPoint)