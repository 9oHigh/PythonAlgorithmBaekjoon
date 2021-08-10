import sys

#하노이탑 재귀함수
def hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        hanoi(N - 1, a, c, b)
        print(a, c)
        hanoi(N - 1, b, a, c)
        
N = int(sys.stdin.readline())
sum = 1

#옮긴 횟수 
for i in range(N - 1):
    sum = sum * 2 + 1
print(sum)

hanoi(N, 1, 2, 3)
