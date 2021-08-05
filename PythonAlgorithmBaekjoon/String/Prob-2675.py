cnt = int(input())


def newPrint(leng, alpha):
    for k in range(leng):
        print(alpha, end='')


for i in range(cnt):
    length, inputs = input().split(' ')
    length = int(length)

    for j in range(len(inputs)):
        newPrint(length, inputs[j])

    print(end='\n')
