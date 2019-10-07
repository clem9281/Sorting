# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap_occurred = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    # I want to get the actual max value from the array, rather than using max I'll manually iterate through, find the max value, and give the user an error if we encounter a negative number
    for element in arr:
        if element < 0:
            return "Error, negative numbers not allowed in Count Sort"
        elif element > maximum:
            maximum = element

    # create an array of max + 1 zeroes
    count_arr = [0] * (maximum + 1)

    for element in arr:
        count_arr[element] += 1

    total = 0
    for i in range(0, maximum + 1):
        temp = count_arr[i]
        count_arr[i] = total
        total += temp

    output = [None] * len(arr)
    for element in arr:
        output[count_arr[element]] = element
        count_arr[element] += 1
    return output
