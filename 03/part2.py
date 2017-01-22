import itertools
from itertools import islice

numValid=0

def isValid(lengths):
    global numValid
    for pair in itertools.combinations(lengths, 2):
        if not all(i <sum(pair) for i in lengths):
            return
    global numValid+=1

with open("p3input.txt") as f:
    while True:
        block=list(islice(f,3))
        if not block: break
        #kind of convoluted
        block_t=list(zip(*([map(int,x.strip().split()) for x in block])))
        for tri in block_t: isValid(tri)

print(numValid)
