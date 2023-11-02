def binary_search_count(lst, item):
    low = 0
    high = len(lst) - 1
    count_search = 0

    while low <= high:
        middle = (high + low) // 2
        kick = lst[middle]
        count_search += 1

        if kick == item:
            return middle, count_search
        if kick > item:
            high = middle - 1
        else:
            low = middle + 1

    return None, count_search


number_list = [1, 3, 5, 7, 9]
result, count = binary_search_count(number_list, 1)
print("index: ", result)
print("count: ", count)
