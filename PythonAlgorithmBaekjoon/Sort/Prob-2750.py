import sys

N = int(sys.stdin.readline())
numbers = []
change = 0

for i in range(N):
    numbers.append(int(sys.stdin.readline()))

# O(n^2)의 시간복잡도를 가진 정렬방식들
# 버블정렬 - 큰 값을 뒤에서부터 쌓아가는 방식
for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

# 삽입정렬 - 거의 사용안함. 정렬의 범위가 점점 늘어난다는 단점이 있음.
for end in range(1,len(numbers)):
    for i in range(end,0,-1):
        if numbers[i-1]>numbers[i]:
            numbers[i-1],numbers[i] = numbers[i],numbers[i-1]

# 선택정렬 - 최솟값을 찾아 가장 앞에서부터 쌓아가는 방식, 반대로도 가능하다.
for i in range(len(numbers)-1):
    minIdx = i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[minIdx]:
            minIdx = j
    numbers[i],numbers[minIdx] = numbers[minIdx],numbers[i]

for i in range(N):
    print(numbers[i])