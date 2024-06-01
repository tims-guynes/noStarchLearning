import math

def BinarySearch(array, target):
    indexHigh = len(array) -1
    indexLow = 0

    while indexLow <= indexHigh:
        indexMid = math.floor((indexHigh + indexLow) / 2)

        if array[indexMid] == target:
            return indexMid
        if array[indexMid] < target:
            indexLow = indexMid + 1
        else:
            indexHigh = indexMid - 1
    return -1

test_list_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(BinarySearch(test_list_01, 7))
print(BinarySearch(test_list_01, 3))