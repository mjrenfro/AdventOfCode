#! /usr/bin/env python


'''Scratch pad area for thoughts

Simplified problem description:
count the number of pairs that satisfy condition X
sum of a given property of two elements is less than an arbitrary
number k

Resource
https://softwareengineering.stackexchange.com/questions/219738/evaluate-all-pair-combinations-in-an-array-for-a-condition-in-n-log-n-time-compl

Obvious solution of unchanged input: O(n^2)

Determining the time complexity
Given the first iteration, the
initial element will have to check length-1
n elements will have to be evaluated
Second iterations: n-1 elements are evaluated
(since the first and second pairing doesn't have to be evaluated)
So forth, sum = [n(n+1)]/2 = O(n^2)

Idea inspired by resource

Sort the input of data by the avail property in decreasing order
Find the first element that has the avail property that is less than the Used
property. Whatever index that is is the number of elements that would be a valid
"partner" for the element
'''

SMALL_INPUT_FILE='smallInput.txt'
INPUT_FILE="input.txt"

#Reads in the input file and correctly populates a "column" based structure
def GetData (fileName):
    data=open(filename, "rt", encoding='utf-8')
    return csv.DictReader(data, delimiter="\t")


class TestSolution(unittest.TestCase):
    def Test_Readin_File(self):


    def Test_Pair_Finding(self):
