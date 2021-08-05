import sys

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

N = int(sys.stdin.readline())
answer = fibonacci(N)
print(answer)