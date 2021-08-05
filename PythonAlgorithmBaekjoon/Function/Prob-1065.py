def counts(number):
    count = 0
    for i in range(1, number+1):
        if i < 100:
            count += 1
        else:
            numbers = list(map(int, str(i)))
            if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
                count += 1
    return count


inputNum = int(input())
print(counts(inputNum))
