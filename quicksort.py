#################################################
# https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78868166210923


def quicksort(arr):
    # print arr
    if len(arr) <= 1:
        return arr

    pivot_idx = len(arr) - 1
    i = 0

    for count in range(len(arr) - 1):
        if i == pivot_idx:
            break
        if arr[i] > arr[pivot_idx]:
            arr[pivot_idx], arr[pivot_idx - 1] = arr[pivot_idx - 1], arr[pivot_idx]
            if i != pivot_idx - 1:
                arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
            pivot_idx -= 1
        else:
            i += 1

    left_arr = quicksort(arr[:pivot_idx])
    right_arr = quicksort(arr[(pivot_idx + 1):])

    output_arr = left_arr + [arr[pivot_idx]] + right_arr
    # print 'Returning: {arr}'.format(arr=output_arr)
    return output_arr


def partition(arr, start, end):
    i = start
    pivot = arr[end]
    print 'pivot: ', pivot
    print 'start: ', start
    print 'end: ', end

    for j in range(start, end):
        print i
        print j
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        print arr

    arr[i], arr[end] = arr[end], arr[i]
    return i


def quicksort_inplace(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1

    if end > start:
        i = partition(arr, start, end)
        quicksort_inplace(arr, start, i - 1)
        quicksort_inplace(arr, i + 1, end)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test_2 = [5, 4, 6, 3, 6, 2, 7, 1, 4, 7, 1, 7, 4]
test_3 = [1]
test_4 = [10, 9, 8, 7, 4, 8, 23, 5]
# print quicksort(test)
# print quicksort(test_2)
# print quicksort(test_3)
# print quicksort(test_4)

quicksort_inplace(test)
print test
