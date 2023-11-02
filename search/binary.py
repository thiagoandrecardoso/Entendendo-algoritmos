def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (high + low) // 2
        kick = lst[middle]
        if kick == item:
            return middle
        if kick > item:
            high = middle - 1
        else:
            low = middle + 1
    return None


number_list = [1, 3, 5, 7, 9]

print(binary_search(number_list, 3))
print(binary_search(number_list, -1))

# Big O: O(log n)
'''
Binary search is an efficient algorithm for finding an element in an ordered list.
'''
