# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        minval = min(arr[i:])
        # TO-DO: swap
        arr[arr.index(minval)], arr[i] = arr[i], minval

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    while True:
        switched = False
        for x in range(len(arr)-1):
            if arr[x] > arr[x+1]:
                switched = True
                arr[x], arr[x+1] = arr[x+1], arr[x]
                # print(arr1)
        if switched is False:
            break
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
