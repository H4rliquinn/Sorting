# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))
    merged_arr += arrA if arrA else arrB
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        arrA = merge_sort(arr[0:len(arr)//2])
        top = (len(arr)//2)
        arrB = merge_sort(arr[top:])
        arr = merge(arrA, arrB)
    return arr


# print(merge_sort([1, 5, 10, 58, 89, 51, 4, 6, 4, 3, 6]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    if arr[start] < arr[mid]:
        arr[start]
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
