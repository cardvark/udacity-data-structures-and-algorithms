#################################################
# https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/71181444620923#


def bubble_sort(arr):
    idx_max = len(arr) - 1
    un_sorted = True

    while un_sorted:
        un_sorted = False
        for i in range(idx_max):
            print arr
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                un_sorted = True
        idx_max -= 1  # This changes to short bubble sort.
    return arr


print bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14])


"""

Short bubble works on the knowledge that the highest num will always be
pushed all the way to the end of the list.

However, the previous last item in the list may not be the next highest.

"""
