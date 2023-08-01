# Book
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        minors = [i for i in array[1:] if i <= pivot]
        bigger = [i for i in array[1:] if i > pivot]
        return quicksort(minors) + [pivot] + quicksort(bigger)


print(quicksort([10, 5, 2, 3]))


# ChatGPT
def quicksort(array):
    if len(array) < 2:
        return array

    # Choice of pivot as the median of three (first, last and middle element).
    mid = len(array) // 2
    pivot = sorted([array[0], array[mid], array[-1]])[1]

    # List partitioning
    left = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + equal + quicksort(right)


# Example of use:
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quicksort(my_array)
print(sorted_array)
