import sys

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)

N = int(sys.stdin.readline())
answer = factorial(N)
print(answer)