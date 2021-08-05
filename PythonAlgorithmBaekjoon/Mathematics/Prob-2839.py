N = int(input())
countlist = []
# 5와 3으로 나누면서 가장 적은 봉지수를 출력해보자
# 만약 5와 3으로 나눌 수 없는 수라면 -1을 출력하자

maxMok = N // 5

if maxMok == 0:
    if N % 3 == 0:
        countlist.append(N // 3)
    else:
        print(-1)
        exit(0)
else:
    for i in range(1, maxMok+1):
        tmp = 0
        tmp = N - (i*5)

        if tmp % 3 != 0:
            if N % 3 == 0:
                countlist.append(N//3)
            continue
        else:
            small = tmp // 3
            countlist.append(i + small)

if not countlist:
    print(-1)
else:
    print(min(countlist))
