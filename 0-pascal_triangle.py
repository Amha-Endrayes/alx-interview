#!/usr/bin/python3
""" 
A Python Module To Generate Pascal's Triangel
"""


def pascal_triangle(n):
    """
    returns a list containg of integers representing Pascal's triangle
    argument: n [int] - size of the pascal triangel    
    """
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
