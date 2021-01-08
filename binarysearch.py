"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or a -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""

    # set the start and end variables for where to look in
    start = 0
    end = len(input_array) - 1

    # while in range of two end points
    while start <= end:
        # get the middle of end points. use floor division to round down
        mid = (start + end) // 2

        # if the middle index value is the value, then return it
        if input_array[mid] == value:
            return mid

        # if the value is less than current value of the middle
        elif value < input_array[mid]:
            # shift the end of search range to be 1 less the mid value
            end = mid - 1

        # otherwise value is more than current value of the middle
        else:
            # then move start of search to 1 more than mid value
            start = mid + 1

    # returning -1 means value was not found
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
