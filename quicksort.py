"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    elements = len(array)

    # Base case
    if elements < 2:
        return array

    # Position of the partitioning element
    current_position = 0

    # Partitioning loop
    for i in range(1, elements):
        if array[i] <= array[0]:
            current_position += 1
            temp = array[i]
            array[i] = array[current_position]
            array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position]
    # Brings pivot to it's appropriate position
    array[current_position] = temp

    # Sorts the elements to the left of pivot
    left = quicksort(array[0:current_position])
    # sorts the elements to the right of pivot
    right = quicksort(array[current_position + 1:elements])

    # Merging everything together
    array = left + [array[current_position]] + right

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
