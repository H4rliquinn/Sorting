# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # print(arr)
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        minval = min(arr[cur_index:])
        minindex = arr.index(minval)
        # print(cur_index, smallest_index, minval, minindex)
        # TO-DO: swap
        arr[minindex] = arr[cur_index]
        arr[cur_index] = minval
        # print(arr)

    return arr


selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
