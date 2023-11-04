# Write a recursive function in Python that calculates the sum of the first 'n' natural numbers.
# Sum = n + (n-1) + (n-2) + ... + 3 + 2 + 1.

# Sum of the first n natural numbers
# It performs a total of 7 operations (4 recursive calls and 3 sums).
def sum_first_natural_numbers(n):
    if n == 0:
        return n
    return n + sum_first_natural_numbers(n - 1)


print(sum_first_natural_numbers(3))


# tail recursion
# The total number of operations will be equal to n + 1
# as recursion occurs until it reaches the base case (n == 0) and then is returned one last time.
def sum_first_natural_numbers_tail(n, acc=0):
    if n == 0:
        return acc
    return sum_first_natural_numbers_tail(n - 1, acc + n)


print(sum_first_natural_numbers_tail(3))
