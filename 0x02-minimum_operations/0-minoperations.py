#!/usr/bin/python3

"""
Given a number n, a module that calculates the fewest number
of operations needed to result in exactly (n) 'H' characters
in a text file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations required to
    duplicate a single character using two operations
    (n) number of times.

    Args:
    @n - number of characters required

    Returns:
    int x - returns minimum number of operations
    required to meet target if possible.
    0 - if n is impossible to achieve

    """

    if type(n) is not int or n <= 1:
        return 0

    operations = 0
    characters = 1
    copyFactor = 1

    while characters < n:
        if n % characters == 0:
            copyFactor = characters
            operations += 1

        if characters != n:
            characters += copyFactor
            operations += 1
        else:
            break

    return operations
