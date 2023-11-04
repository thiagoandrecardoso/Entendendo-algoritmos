def tail_recursive_fibonacci(n, current=0, next_=1, count=0):
    if count == n:
        return current
    else:
        return tail_recursive_fibonacci(n, next_, current + next_, count + 1)


print(tail_recursive_fibonacci(6))  # 1, 1, 2, 3, 5, 8
