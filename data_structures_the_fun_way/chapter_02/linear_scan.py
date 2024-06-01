def LinearScan(array, target):
    i = 0
    while i < len(array):
        if array[i] == target:
            return i
        i = i + 1
    return -1

test_array_01 = [3, 11, 9, 37, 7, 8, 1, 21, 5, 17, 31]

print(LinearScan(test_array_01, 5))
print(LinearScan(test_array_01, 21))