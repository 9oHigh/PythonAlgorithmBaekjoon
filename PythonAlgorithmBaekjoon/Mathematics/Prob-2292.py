# 1 / 1+ 6*1 / 1 + 6*3 / 1 + 6*6 /1+ 6*10
#   1       / 2      /  3      /  4
N = int(input())

multi = 0
plus = 1
Start = 1
while True:
    Start += (6 * multi)
    if Start >= N:
        print(plus)
        break
    multi = plus
    plus += 1
