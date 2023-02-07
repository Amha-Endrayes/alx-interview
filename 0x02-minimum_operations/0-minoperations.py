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

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        j = 2
        while j <= i // 2:
            if dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1
            j += 1
    return dp[n]
