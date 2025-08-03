# Purpose of posting: SSHJerry forgets things overtime. This is a good refresher for concepts not used in the everyday work environment

"""This Quick Sort implementation utilized the choice of the pivot as the last element in block.
A better method would've been to do a Median-Of-Three as a choice of pivot.
This involves picking the first, middle, and last index of array, sort them, and pick the middle value as the pivot of main array. 
Worse case: O(N^2) | Average Case: O(n log n)"""
def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    if right - left > 1:
        mid = partition(arr, left, right - 1)
        quicksort(arr, left, mid)
        quicksort(arr, mid + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    partIndex = left
    for i in range(left, right):
        print('IN FOR LOOP')
        print(f'array: {arr}\tleft: {left}\tright: {right}, AND pivot: {pivot} AND partIndex: {partIndex}')
        if arr[i] < pivot:
            print('IS SWAPPING\n')
            print(f'BEFORE: arr[i]: {arr[i]}, arr[partIndex]: {arr[partIndex]}\t')
            arr[i], arr[partIndex] = arr[partIndex], arr[i]
            print(f'AFTER: arr[i]: {arr[i]}, arr[partIndex]: {arr[partIndex]}\n')
            partIndex += 1
    print('Last Swap')
    print(f'BEFORE: arr[partIndex]: {arr[partIndex]}, arr[right]: {arr[right]}\t')
    arr[partIndex], arr[right] = arr[right], arr[partIndex]
    print(f'AFTER: arr[partIndex]: {arr[partIndex]}, arr[right]: {arr[right]}\n')

    print(f'End of Parition Method, Returning {partIndex}\t Current Array: {arr}')
    return partIndex
  
#------------------------------------------------------------------------
def merge(listOne, listTwo, mainList):
    i = j = 0
    while i < len(listOne) or j < len(listTwo):
        print(i, j)
        if j == len(listTwo) or (i < len(listOne) and listOne[i] < listTwo[j]):
            mainList[i + j] = listOne[i]
            i += 1
        else:
            mainList[i + j] = listTwo[j]
            j += 1

def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    middle = n // 2
    left = arr[:middle]
    right = arr[middle:]
    mergesort(left)
    mergesort(right)
    merge(left, right, arr)


#Test 1:
quicksort([10, 1, 9, 2, 8, 3, 7, 4, 5])
mergesort([10, 1, 9, 2, 8, 3, 7, 4, 5])
