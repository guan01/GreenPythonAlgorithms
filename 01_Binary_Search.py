def binary_search(array, target):
    leftindex = 0
    rightindex = len(array) - 1
    mid = rightindex // 2

    while leftindex <= rightindex:
        mid = (leftindex + rightindex) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            leftindex = mid + 1
        elif array[mid] > target:
            rightindex = mid - 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 22, 500, 501, 502, 800, 820, 933], 6))
      



























