N = int(input())
#리스트에 한번에 입력받는 방법 list(map(변수형,input().split()))
alolist = list(map(int, input().split()))
answer = 0
#1로 나누면 항상 0
cnt = 1

for i in alolist:
    #1을 제외하고
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        answer += 1
    cnt = 1
print(answer)
