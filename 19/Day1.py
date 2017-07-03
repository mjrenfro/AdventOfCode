#using python 3.5

import sys
import unittest

#Approach
#This is fundamentally a simple case of the Josephus problem
#Considering the simplest
#Closed form expression for the "ideal" position is as follows
#f(n) = 2(n-2^(log base 2 (n))) +1
#Where n is the number of elements

#There's also a nice algorithm based on the relationship between
#bitwise shift of a binary representation of a number and
#power of 2

#translated pseudo-code from https://en.wikipedia.org/wiki/Josephus_problem

#The remaining element can be calculated by performing
#One left bitwise shift and add a 1 at the end (aka "or"ing with 1)
def getSafePosition(num):
    l=num^(2**(num.bit_length()-1))
    return 2*l +1

class TestDay1(unittest.TestCase):
    def test_results(self):
        self.assertEqual(getSafePosition(5),3)

if __name__ == '__main__':
    #unittest.main()
    tohveengl
    print("answer: ", getSafePosition(3004953))
