X = int(input())

i = 0
while X > 0:
    X -= i
    i += 1

X = X + i - 1
res = str(X) + '/' + str(i-X)

if i % 2 == 0:
    res = str(i - X) + '/' + str(X)

print(res)
