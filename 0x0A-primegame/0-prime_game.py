#!/usr/bin/python3
"""
Python module for determining the winner of a game where 2 players
play a game with consecutive integers starting from 1 up to n.
Players take turns choosing primes and removing their multiples.

Winner is player who makes last move.
"""


def isWinner(x, nums):
    """
    Parameters:
    x - rounds
    nums - numbers list

    Returns:
    winner - Ben or Maria
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    removes multiples
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
