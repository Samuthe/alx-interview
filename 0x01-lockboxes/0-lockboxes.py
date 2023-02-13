#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
a) No. of locked boxes -> n
b) boxes are numbered from 0 to n - 1
c) each box may contain a key to other boxes
d) method to determine if all boxes can be opened
e) There can be keys that do not have boxes
f) The first box boxes[0] is unlocked
g) Return True if all boxes can be opened, else return False
"""
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while (True):

        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not (len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
