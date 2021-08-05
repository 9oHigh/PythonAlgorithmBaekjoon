import sys

def isalone(number):
    if number == 1:
        return False

    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if isalone(i):
        print(i)
