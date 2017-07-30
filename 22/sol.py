#! /usr/bin/env python
import sys
import unittest
import re
import itertools

'''Scratch pad area for thoughts

Determining the time complexity
First iteration: n elements are evaluated
Second iterations n-1 elements are evaluated
(since the first and second element pairing doesn't have to be evaluated)
So forth: n-2, n-3, n-4... sum = [n(n+1)]/2 = O(n^2)
'''

SMALL_INPUT_FILE='smallInput.txt'
INPUT_FILE="input.txt"

def GetCoordinates(uri):
    matches=re.match(r".+x(\d+)-y(\d+)",uri )
    return [int(matches.group(1)), int(matches.group(2))]

def GetNumericMemory(string_memory):
    return int(re.match(r"(\d+)T", string_memory).group(1))

#Reads in the input file and correctly populates a "column" based structure
def GetData (fileName):
    machines=[]
    with open(fileName) as f:
        for i, line in enumerate(f):

            #ignoring the 'terminal cmd' and the headers by starting at line 2
            if i>1:
                machine_info=line.split()
                unparsed_uri, unparsed_used, unparsed_available=machine_info[0], machine_info[2], machine_info[3]
                #get the coordinates
                coordinates=GetCoordinates(unparsed_uri)

                #get the used, and available
                used, available=GetNumericMemory(unparsed_used), GetNumericMemory(unparsed_available)

                machines.append([coordinates, used, available])
    return machines

def CountNumPairs(machines_info):
    pair_count=0
    for machine_a, machine_b in list(itertools.permutations(machines_info,2)):
        if machine_a[2]-machine_b[1] >-1 and machine_b[1]>0:
            pair_count+=1
    return pair_count


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(CountNumPairs(GetData(SMALL_INPUT_FILE)), 5)

if __name__ == '__main__':
    #unittest.main()
    print(CountNumPairs(GetData(INPUT_FILE)))
