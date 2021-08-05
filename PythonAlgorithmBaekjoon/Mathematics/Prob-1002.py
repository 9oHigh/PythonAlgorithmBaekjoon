import math

testCase = int(input())

for i in range(testCase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if D == 0:
       if r1 == r2: print(-1)
       else: print(0)
    else:
       if D == r1 + r2 or D == abs(r1-r2): print(1)
       elif D < r1 + r2 and D > abs(r1-r2): print(2)
       else: print(0)
