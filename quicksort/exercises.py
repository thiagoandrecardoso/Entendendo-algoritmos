# Page 90

"""
Create a multiplication table with all the elements of the array. So, if your array is [2, 3, 7, 8, 10],
you will first multiply each element by 2. Then you will multiply each element by 3 and then by 7, and so on.
"""


def create_multiplication_table(arr):
    table = []
    for num in arr:
        row = []
        for element in arr:
            row.append(num * element)
        table.append(row)
    return table
