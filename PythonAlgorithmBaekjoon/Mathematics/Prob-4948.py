import sys
import math

Max = 123456
eratos = [1] * (2 * Max + 1)

eratos[0] = 0
eratos[1] = 0

for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        print(sum(eratos[N+1:(2*N)+1]))
