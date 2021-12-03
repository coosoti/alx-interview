#!/usr/bin/python3
"""
this module contains a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    determines if all boxes can be opened
    @boxes: list of lists
    Returns: True or False
    """
    n = len(boxes)
    stack = [0]
    unlocked_box = [1] + [0] * (n - 1)
    i = 0

    if n == 0:
        return True
    while stack:
        j = stack.pop()
        for index in boxes[j]:
            if index > 0 and index < n and unlocked_box[index] == 0:
                unlocked_box[index] = 1
                stack.append(index)
        i = i + 1
    if 0 in unlocked_box:
        return False
    return True
