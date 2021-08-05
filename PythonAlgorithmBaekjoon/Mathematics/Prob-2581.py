import sys
#input()은 읽는 속도가 굉장히 느리다
#따라서 sys.stdin.readline()
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

alolist = []
cnt = 1

for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        alolist.append(i)
    cnt = 1

if not alolist:
    print(-1)
else:
    print(sum(alolist))
    print(min(alolist))
