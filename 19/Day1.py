#using python 3.5

import sys
import unittest

#Approach
#This is fundamentally a simple case of the Josephus problem

#In this case "k" (the count size) =2 and "n" is the puzzle input
#Wikipedia has the closed form solution for this exact case.
#The closed form expression for the "ideal" position is as follows:
#      f(n) = 2(n-2^(log base 2 (n))) +1


#Another formula for this case:
#     f(N)= 2L +1 where N=2^M +L and 0 <= L < 2^M
#The formula can be calculated by removing the
#highest bit of N and then "xor"ing with the smallest number
#that can be represented with the same num of bits as N

def getSafePosition(num):
    l=num^(2**(num.bit_length()-1))
    return 2*l +1

class TestDay1(unittest.TestCase):
    def test_results(self):
        self.assertEqual(getSafePosition(5),3)

if __name__ == '__main__':
    #unittest.main()
    print("answer: ", getSafePosition(3004953))
