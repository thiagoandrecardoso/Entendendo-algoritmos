# Sum all elements of an array using loop. O(N)
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total


print(sum_list([2, 4, 6]))


# The same example, now using recursion. O(N)
# Exe: 4.1
def sum_recursive(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_recursive(lst[1:])


print(sum_recursive([2, 4, 6]))


# Write a recursive function that counts the number of items n a list.
# Exe: 4.2
def numbers_items(lst):
    if not lst:
        return 0
    return 1 + numbers_items(lst[1:])


print(numbers_items([2, 4, 6]))


# Find the highest value in a list using recursion
# Exe: 4.3 | DIVISION AND CONQUEST is not used here.
def highest_value(lst):
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[1]:
        return highest_value(lst[:1] + lst[2:])
    else:
        return highest_value(lst[1:])


print(highest_value([2, 4, 3]))


# Exe: 4.3 | DIVISION AND CONQUEST is use here.
def find_highest_recursive(lst, index=0):
    if index == len(lst) - 1:
        return lst[index]
    else:
        current_value = lst[index]
        next_value = find_highest_recursive(lst, index + 1)
        return max(current_value, next_value)


print(find_highest_recursive([2, 4]))
