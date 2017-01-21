import re
from itertools import islice

filename='p3input.txt'
inputDims=open(filename)
numValid=0
block=[]

def readInDimensions():
    global inputDims
    nextDim=inputDims.readline().rstrip()
    if nextDim =="":
        return -1
    return nextDim

def readInBlocks():
    global block


    n=list(islice(inputDims,3))
    tri=[x.strip().split() for x in n]
    tri=list(zip(*tri))

    block=tri

def isValid(dims):
    dims=dims.strip()
    lengths=re.split('\s+',dims)
    for idx,l in enumerate(lengths):
        lengths[idx]=int(l)
    valid=True
    if lengths[0]+lengths[1]<=lengths[2]:
        valid=False
    elif lengths[1]+lengths[2]<=lengths[0]:
        valid =False
    elif lengths[2]+lengths[0]<=lengths[1]:
        valid =False
    else:
        pass
    return valid
def isValid_block(tri):
    lengths=[0]*3

    for idx, l in enumerate(list(tri)):
        lengths[idx]=int(l)
    valid = True
    if lengths[0]+lengths[1]<=lengths[2]:
        valid=False
    elif lengths[1]+lengths[2]<=lengths[0]:
        valid =False
    elif lengths[2]+lengths[0]<=lengths[1]:
        valid =False
    else:
        pass
    return valid


#part 2
def checkValidBlocks():
    global numValid
    readInBlocks()
    while  block!=[]:

        for tri in block:
            print()
            if isValid_block(tri):
                numValid+=1

        readInBlocks()

#part 1
def checkValidTriangles():
    global numValid
    temp=readInDimensions()
    while temp!=-1:
        if isValid(temp):
            numValid+=1
        temp=readInDimensions()

if __name__ == "__main__":
    checkValidBlocks()
    print (numValid)
