#################################################
# https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78825770750923


def comparison(arr1, arr2):
    new_arr = []

    i = 0
    y = 0

    while i < len(arr1) and y < len(arr2):
        if arr1[i] <= arr2[y]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[y])
            y += 1

    output = new_arr + arr1[i:len(arr1)] + arr2[y:len(arr2)]
    print output
    return output


def recursive_merge(arr):
    # print arr
    if len(arr) > 1:
        mid = len(arr) / 2
        left = arr[0:mid]
        right = arr[mid:]

        left = recursive_merge(left)
        right = recursive_merge(right)

        return comparison(left, right)
    else:
        return arr


def merger(split_arr):
    start_idx = 0 if len(split_arr) % 2 == 0 else 1
    new_arr = []

    if start_idx == 1:
        new_arr.append(split_arr[0])

    carry = None
    for i in range(start_idx, len(split_arr)):
        if not carry:
            carry = split_arr[i]
        else:
            new_arr.append(comparison(carry, split_arr[i]))
            carry = None
    return new_arr


def merge_sort(arr):
    split_arr = [[item] for item in arr]

    while len(split_arr) > 1:
        print split_arr
        split_arr = merger(split_arr)

    return split_arr[0]


# print merge_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14])
# print merge_sort([5, 5, 5, 5, 5, 8, 10])
# print merge_sort([1])
print merge_sort([21, 4, 1, 3, 9, 20, 25])

print recursive_merge([21, 4, 1, 3, 9, 20, 25, 6, 21, 14])
print recursive_merge([5, 5, 5, 5, 5, 8, 10])
print recursive_merge([1])
