def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))
# Big O = O(n).


# Tail recursive:
def tail_recursive_factorial(n, acc=1, c=0):
    c += 1
    if n == 0:
        return acc
    else:
        return tail_recursive_factorial(n - 1, n * acc, c)


print(tail_recursive_factorial(5))

