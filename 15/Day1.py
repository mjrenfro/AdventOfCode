import re

#Determines the earliest time that
#a sequence of "discs" is such that a capsule can fall through
#to the bottom.

#Reduction:
    #when does disc1 (position+1)%size1==0
    #and
    #when does disc2 (position+2)%size2==0
    #...


#Package the total # of positions and the starting position
#into an array
def parseDiscs(discs):
    discDetails=[]
    for disc in discs:
        totalPositions=int(re.compile('(\d+) positions').findall(disc)[0])
        currentPosition=int(re.compile('position (\d+)').findall(disc)[0])
        discDetails.append([totalPositions, currentPosition])
    return discDetails

#first combination
def earliest_lineup(disc_details):
    dropTime=0
    makesThrough=True
    while True:
        for idx, detail in enumerate(disc_details):
            # print ("detail: ", detail)
            size, position=detail
            if (position+idx+1+dropTime)%size !=0:
                makesThrough=False
        if makesThrough==True:
            break
        dropTime+=1
        makesThrough=True
    return dropTime

#read in input
with open('input2.txt') as f:
    unparsedDiscs=[l.rstrip('\n') for l in f.readlines()]
    soonestTime=earliest_lineup(parseDiscs(unparsedDiscs))
    print("Soonest Time: ",soonestTime)
