# Using breadth first search to explore the constrained frontier

import hashlib
from collections import deque
import sys
import unittest

open_letters=['b','c','d','e','f']

dirs=[[(0,-1),'U'], [(0,1),'D'], [(-1,0),'L'], [(1,0),'R']]

def Add(p1, p2):
    return tuple(map(sum, zip(p1,p2)))

#returns the first 4 letters of the MD5 hash for
#the given string
def SubHash(path, passcode):
    return hashlib.md5((passcode+path).encode('utf-8')).hexdigest()[:4]

#returns a subset of dirs
def OpenNeighbors(path, point, passcode):
    subHash=SubHash(path, passcode)

    return [ [Add(d[0], point), d[1]] for d in dirs if (subHash[dirs.index(d)] in open_letters) ]

def IsValid(point):
    r,c = point

    return r >= 0 and r < 4 and c >= 0 and c <4

def NextMoves(path, point, passcode):
    soFar=[(path+d[1], d[0]) for d in OpenNeighbors(path, point, passcode) if  IsValid(d[0])]

    return soFar

#bfs because dfs is not complete
def Search (passcode):
     #only keeps track of minimum
     frontier =("")

     #upper left hand corner
     start =(0,0)

     #lower right hand corner
     goal = (3,3)

     queue=deque([('',start)])
     while queue:

        path, pos= queue.popleft()
        if pos == goal:
            frontier=path
        else:
            if (len(path)<len(frontier)-1 or frontier ==""):
                queue.extend(NextMoves(path, pos, passcode))
     return frontier

class TestDay1(unittest.TestCase):
    def test_results(self):
        self.assertEqual(Search("ihgpwlah"), "DDRRRD")
        self.assertEqual(Search("kglvqrro"), "DDUDRLRRUDRD")
        self.assertEqual(Search("ulqzkmiv"), "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

if __name__=='__main__':
    #unittest.main()
    print("answer ", Search ("pxxbnzuo"))
