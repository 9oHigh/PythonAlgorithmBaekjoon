#A는 고정비용
#B는 가변 비용
#C는 노트북 가격
A, B, C = map(int, input().split())

#불가능 조건
if B >= C:
    print(-1)
else:
    print(int(A/(C-B))+1)
