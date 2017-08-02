#! /usr/bin/env python
import sys
import unittest
import re
from itertools import permutations
from copy import deepcopy

'''Scratch pad area for thoughts

Determining the time complexity
First iteration: n elements are evaluated
Second iterations n-1 elements are evaluated
(since the first and second element pairing doesn't have to be evaluated)
So forth: n-2, n-3, n-4... sum = [n(n+1)]/2 = O(n^2)
'''

SMALL_INPUT_FILE='smallInput.txt'
INPUT_FILE='input.txt'

def GetCoordinates(uri):
    matches=re.match(r".+x(\d+)-y(\d+)",uri )
    return [int(matches.group(1)), int(matches.group(2))]

def GetNumericMemory(string_memory):
    return int(re.match(r"(\d+)T", string_memory).group(1))

#TODO: use list comprehension
def UnravelArray(array):
    linear_array=[]
    for c, row in enumerate(array):
        for r,element in enumerate(row):
                linear_array.append([[r,c],element])

    return linear_array

#Reads in the input file and correctly populates a 2d array
#Assumption is that the input file is organized by row order
#where each element is a list of a machine's
#coordinates, used data, available data, whether or not it is the goal node

def GetData (fileName):
    network=[]

    with open(fileName) as f:
        rowIndex =0
        row=[]
        for i, line in enumerate(f):

            #ignoring the 'terminal cmd' and the headers by starting at line 2
            if i>1:

                machine_info=line.split()
                unparsed_uri,unparsed_capacity, unparsed_used, unparsed_available=machine_info[0], machine_info[1], machine_info[2], machine_info[3]

                #get the coordinates
                coordinates=GetCoordinates(unparsed_uri)

                #get the used, and available
                capacity, used, available=GetNumericMemory(unparsed_capacity), GetNumericMemory(unparsed_used), GetNumericMemory(unparsed_available)

                #if part of the same row, then just add to the current row
                if coordinates[0]==rowIndex:
                    row.append([used, available])

                #if part of a different row, append current row to network and start new row
                else:
                    rowIndex+=1
                    network.append(row)
                    row=[[capacity,used, available]]

        #append the last row
        network.append(row)

        #Indicate the target node
        network[0][len(row)-1].append(True)
    return network

def GetNextMoves(network):
    NextMoves=[]
    for a, b in list(permutations(UnravelArray(network),2)):

        if a[1][1]>=b[1][0] and b[1][0]>0:
            NextMoves.append([a,b])
    return NextMoves

#input: list of possible nodes that can be swapped, and current network
#output: list of possible networks after the swaps take place

def GetNextNetworks(next_moves, current_network):
    NextNetworks=[]
    for next_move in next_moves:
        next_network=deepcopy(current_network)
        x0,y0 = next_move[0][0]
        x1,y1=next_move[1][0]
        #data swap of moves
        temp_used=next_network[x0][y0][0]
        next_network[x0][y0][0]=next_network[x1][y1][0]
        next_network[x1][y1][0]=temp_used
        NextNetworks.append(next_network)
    return NextNetworks


def CountNumPairs(network):
    return len(GetNextMoves(network))
def ExploreFrontier(paths):
    pass

# Approach: Modified BFS, no backtracking where the graph is the possible states
# the network can assume from swapping memory.
# During the search, a list of previous network states is stored so that the
# backtracking can be prevented.
#
# Input: The network's initial state represented by a list of lists
# def Explore(network):

def GetFewestMoves(network):
    frontier=[[network]]

    #assumes that the solution is possible
    while len(frontier)!=0:
        print("frontier:", frontier)
        for idx in range(len(frontier)):
            path=frontier.pop(idx)
            current_network=path[0]

            #Is this the ending case
            try:
                if current_network[0][0][2]==True:
                    return len(path)
            except:
                pass

            nextNetworks=GetNextNetworks(GetNextMoves(current_network), current_network)
            for network in nextNetworks:
                print("next network: ", network)

            #no backtracking
            for non_dup_network in [network for network in nextNetworks if network not in path]:
                path_copy=deepcopy(path)
                path_copy.append(non_dup_network)
                frontier.append(path_copy)


class TestSolution(unittest.TestCase):
    def test_readin (self):
        self.assertEqual(0,0)
    def test_day1(self):
        self.assertEqual(CountNumPairs(GetData(SMALL_INPUT_FILE)), 7)
    def test_day2(self):
        self.assertEqual(GetFewestMoves(GetData(SMALL_INPUT_FILE)),7)



if __name__ == '__main__':
    unittest.main()
    #print(GetData(SMALL_INPUT_FILE))
    #print(CountNumPairs(GetData(INPUT_FILE)))
