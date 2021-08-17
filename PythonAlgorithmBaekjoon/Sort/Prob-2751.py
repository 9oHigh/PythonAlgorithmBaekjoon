import sys

N = int(sys.stdin.readline())
numbers = []
change = 0

for i in range(N):
    numbers.append(int(sys.stdin.readline()))

#총 3가지의 NlogN의 시간복잡도를 지닌 정렬 알고리즘을 정리해 보자.

'''
1. Quick Sort - Devide and Conquer + recursion
-   pivot이라는 기준값을 활용하는 방법(앞,뒤,중앙 등등)으로 어떠한 값을 
    pivot값으로 정하냐에 따라 효율이 차이가 날 수 있다( O(N^2)의 시간복잡도를 가질 수도 있다 ).
    정해진 pivot값을 기준으로 한쪽에는 작은 값을 한쪽에는 큰 값을 두고 비교, 정렬을 반복
    하게 된다.
'''
#기본적인 Python Code
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] #중앙에 위치한 값을 pivot으로 설정
    lesserArr, equalArr, greaterArr = [], [], []
    for num in arr:
        if num < pivot:
            lesserArr.append(num)
        elif num > pivot:
            greaterArr.append(num)
        else:
            equalArr.append(num)
    return quickSort(lesserArr) + equalArr + quickSort(greaterArr)

#최적화된 Python Code : partion을 활용
def quickSort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
'''
2. Merge Sort - Devide and Conquer + recursion
-   주어진 배열을 원소가 하나 밖에 남지 않을 때까지 지속적으로 반으로 쪼갠 뒤에
    다시 크기순으로 재배열 하면서 원래 배열의 사이즈로 합치는 정렬 알고리즘
    리스트의 slice notation(arr[start:end])를 이용하여 간단하게 사용할 수 있지만
    slice를 이용할 때 배열의 복제가 일어나므로 메모리 효율에 좋지 않음
    따라서 배열을 매번 생성하지 않고 인덱스에 접근해 업데이트하는 방법을 사용하자.
''' 
# 배열 생성
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    lowArr = mergeSort(arr[:mid])
    highArr = mergeSort(arr[mid:])

    mergedArr = []
    l = h = 0
    while l < len(lowArr) and h < len(highArr):
        if lowArr[l] < highArr[h]:
            mergedArr.append(lowArr[l])
            l+=1
        else:
            mergedArr.append(highArr[h])
            h+=1
    mergedArr += lowArr[l:]
    mergedArr += highArr[h:]
    return mergedArr

#인덱스 접근
def mergeSort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
'''
Heap Sort - Complete Binary Tree / Array
-   각 노드의 값이 자식 노드의 값보다 크거나 같다면 최대힙(Max Heap)
    각 노드의 값이 자식 노드의 값보다 작거나 같다면 최소힙(Min Heap)
    힙을 배열 형식으로 표현하게 되면 
    leftIndex = 2*index+1
    rightIndex = 2*index+2 와 같은 관계를 지닌다.
-   Heap Sort를 위해서는 Heapify를 통해 힙의 성질을 지속적으로
    만족하게 만들어야한다.
'''
# Heapify - 힙의 성질을 그대로 유지할 수 있게 배열을 만들어 줘야한다.
def heapify(unsorted, index, heapSize):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heapSize and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heapSize and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heapSize)

# Heap Sort
def heapSort(unsorted):
    n = len(unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

    return unsorted

heapSort(numbers)

for i in range(N):
    print(numbers[i])