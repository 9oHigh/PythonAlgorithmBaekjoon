import sys

N = int(sys.stdin.readline())

numberlist = []
cut = 2

if N == 1:
    exit(0)
else:
    while True:
        if N % cut == 0:
            numberlist.append(cut)
            if cut == 2:
                N = N - N//cut
            else:
                N = N // cut
        else:
            cut += 1
        if N == 1:
            break

for i in range(len(numberlist)):
    print(numberlist[i])
