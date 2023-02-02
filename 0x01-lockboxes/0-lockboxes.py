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

    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False
    for k in range(len(boxes)):
        boxes_checked = False
        for idx in range(len(boxes)):
            if k in boxes[idx] and k != idx:
                boxes_checked = True
                break
        if not boxes_checked:
            return False
    return True
