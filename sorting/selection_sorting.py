def search_minor(arr):
    minor = arr[0]
    minor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i
    return minor_index


def sorting_by_selection(arr):
    new_arr = []
    for i in range(len(arr)):
        minor = search_minor(arr)
        new_arr.append(arr.pop(minor))
    return new_arr


print(sorting_by_selection([5, 3, 6, 2, 10]))
