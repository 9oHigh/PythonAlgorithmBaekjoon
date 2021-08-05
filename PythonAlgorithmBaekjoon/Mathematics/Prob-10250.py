case = int(input())
#H는 층수, W는 최대호수, N은 지정호수
for i in range(0, case):
    H, W, N = map(int, input().split())
    dong = 0
    ho = 0
    if N % H == 0:
        dong = H * 100
        ho = N // H
    else:
        dong = (N % H) * 100
        ho = 1+N//H

    print(dong+ho)
