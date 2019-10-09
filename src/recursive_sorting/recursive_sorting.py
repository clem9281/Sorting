# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    counter = 0
    while len(arrA) > 0 and len(arrB) > 0:
        currentA = arrA[0]
        currentB = arrB[0]
        if currentA < currentB:
            merged_arr[counter] += currentA
            arrA.pop(0)
            counter += 1
        else:
            merged_arr[counter] += currentB
            arrB.pop(0)
            counter += 1
    while len(arrA) > 0:
        merged_arr[counter] += arrA[0]
        arrA.pop(0)
        counter += 1
    while len(arrB) > 0:
        merged_arr[counter] += arrB[0]
        arrB.pop(0)
        counter += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # print({"arr": arr})
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


print(merge_sort(arr1))
