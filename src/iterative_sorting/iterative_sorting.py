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
    while True:
        switched = False
        for x in range(len(arr)-1):
            if arr[x] > arr[x+1]:
                switched = True
                temp = arr[x+1]
                arr[x+1] = arr[x]
                arr[x] = temp
                # print(arr1)
        if switched is False:
            break
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
