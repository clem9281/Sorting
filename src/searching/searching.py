# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        print(arr, middle, low, high)
        # if arr[middle] == target:
        #   return middle
        if arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            return middle
    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2
    if len(arr) == 0 or high < low:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    elif arr[middle] < target:
        low = middle + 1
        return binary_search_recursive(arr, target, low, high)
    elif arr[middle] > target:
        high = middle - 1
        return binary_search_recursive(arr, target, low, high)
    elif arr[middle] == target:
        return middle



