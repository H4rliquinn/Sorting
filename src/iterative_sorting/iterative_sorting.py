# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        minval = min(arr[cur_index:])
        minindex = arr.index(minval)
        # TO-DO: swap
        arr[minindex] = arr[cur_index]
        arr[cur_index] = minval

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    curr_index = 0
    for x in range(arr-1):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
