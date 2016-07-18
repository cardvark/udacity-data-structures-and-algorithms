#################################################
# https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78812066010923

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value, min_idx=None, last_idx=None):
    if not min_idx:
        min_idx = 0
    if not last_idx:
        last_idx = len(input_array) - 1

    mid_idx = int(min_idx + (last_idx - min_idx) / 2)
    check_val = input_array[mid_idx]

    if len(input_array[min_idx:last_idx + 1]) == 1 and value != check_val:
        return -1

    if value == check_val:
        return mid_idx
    elif value > check_val:
        return binary_search(input_array, value, mid_idx + 1, last_idx)
    else:
        return binary_search(input_array, value, min_idx, mid_idx - 1)

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
