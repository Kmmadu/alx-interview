#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    takes an argument n and returns a list of lists
    """
    if n <= 0:
        return []
    tria = [[1]*(i+1) for i in range(n)]
    for x in range(n):
        for y in range(1, x):
            tria[x][y] = tria[x-1][y-1] + tria[x-1][y]
    return tria
