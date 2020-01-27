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
        arrB = merge_sort(arr[(len(arr)//2):])
        arr = merge(arrA, arrB)
    return arr


# print(merge_sort([1, 5, 10, 58, 89, 51, 4, 6, 4, 3, 6]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    while start <= mid and mid <= end:
        if arr[start] < arr[mid]:
            start += 1
        else:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1
    return arr


# print(merge_in_place([1, 4, 6, 2, 3, 5], 0, 3, 5))


def merge_sort_in_place(arr, l, r):
    if len(arr) < 2:
        return arr
    if r-l < 1:
        return l, r
    else:
        mid = (r-l)//2
        posA = merge_sort_in_place(arr, l, l+mid)
        posB = merge_sort_in_place(arr, l+mid+1, r)
        merge_in_place(arr, posA[0], posB[0], posB[1])
    if posA[0] == 0 and posB[1] == len(arr)-1:
        return arr
    else:
        return posA[0], posB[1]

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
