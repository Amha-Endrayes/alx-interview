#!/usr/bin/python3
""" 
A Python Module To Generate Pascal's Triangel
"""


def pascal_triangle(n):
    """
    Returns a list containig a list of integers representing
    Pascal's triangle of size n.
    
    argument: n [int] - size of the triangle
    
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
