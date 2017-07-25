#using python 3.5

import sys
import unittest
from collections import deque
import numpy as np
import time

#https://github.com/tomkooij/AdventOfCode/blob/master/aoc2016/day19.py
#tom's code...need to figure out better time complexity solution
def getSafePosition(elfs):

    elfs = list(range(1, elfs+1))
    middle = len(elfs) // 2
    left, right = deque(elfs[:middle]), deque(elfs[middle:])

    while True:
        # remove middle item
        if len(left) > len(right):
            left.pop()
        else:
            #more efficient than 'del'ing or 'pop(0)'' ing
            right.popleft()

        # if right half is empty --> finished

        if not right:
            return left.pop()

        # rotate
        left.append(right.popleft())
        right.append(left.popleft())


class TestDay2(unittest.TestCase):
    def test_results(self):
        self.assertEqual(getSafePosition(5),2)

if __name__ == '__main__':

    start=time.time()
    print(getSafePosition(3004953))
    end=time.time()
    print ("Time: ", end-start)
