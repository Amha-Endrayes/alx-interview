#!/usr/bin/python3

"""
A python module that solves a box puzzel.
Puzzel:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Given a set of boxs, this module checks if all boxes
can be oppened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
    boxes (list of lists): A list of lists where each sublist represents
    a box and contains keys to other boxes. A key with the same number as
    a box opens that box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """

    opened = [False] * len(boxes)  # Keep track of which boxes are unlocked.
    opened[0] = True  # The first box is assumed to be unlocked.
    stack = [0]  # The boxes to be checked for more keys.
    while stack:  # Repeat until all boxes have been checked.
        box = stack.pop()
        for key in boxes[box]:
            if not opened[key]:  # If the box has not been unlocked yet.
                opened[key] = True  # Mark the box as unlocked.
                stack.append(key)  # Add the box to be checked for more keys.
    return all(opened)
