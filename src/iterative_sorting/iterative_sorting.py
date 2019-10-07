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

    # add 1 to each element at the index of the main array element: now count_arr holds an array where each index is like a key, and the element at that index is like a value indicating the count of that element in our original array
    for element in arr:
        count_arr[element] += 1

    # we know how many of each element we have, but really we want to know what index each element should start to be stored at. Start at 0, and we want index 0 to hold the value 0. Then add the count of each element as we move through the array
    total = 0
    for i in range(0, maximum + 1):
        temp = count_arr[i]
        count_arr[i] = total
        total += temp

    # go back through the original array. For each element, go to that index in count_arr (count_arr[element]), and the value there is the index of output where element should be stored. Don't forget to iterate that value by one so you start at the next open slot on the next pass
    output = [None] * len(arr)
    for element in arr:
        output[count_arr[element]] = element
        count_arr[element] += 1
    return output


# try this again
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        # start one to the left of i and move backwards
        for j in range(i - 1, -1, -1):
            if temp < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(insertion_sort(arr1))
