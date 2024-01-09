#!/usr/bin/python3
"""Define write_file"""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    previous_row = pascal_triangle(n - 1)
    lst = [1]

    for i in range(1, n - 1):
        lst.append(previous_row[-1][i - 1] + previous_row[-1][i])
    lst.append(1)
    return previous_row + [lst]
