#Problem description can be found @ https://adventofcode.com/2016/day/1

#Approach to part 2
#Find the first intersection by keeping track of only the beginning and
#ending coordinates of each 'walk'

import re
from operator import itemgetter

plan_input="L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"

#Reorganizes the input
def populatePlan(plan):
    for inst in re.split(', ', plan_input):
        plan.append([inst[:1], int(inst[1:])])

def updateOrientation(dir, orientation):
    #update the direction
    if dir=='L':
        return (orientation-1)%4
    else:
        return (orientation+1)%4

#returns which axis the segment is parallel to
def getAxis(point_a, point_b):
    #vertical (y-axis) =1, horizontal (x-axis) =0
    return int(point_a[0]==point_b[0])

def invertAxis(axis):
    return int(not bool(axis))

def findJunction(history):
    seg, axis=history[0]
    opp_axis=invertAxis(axis)

    perpendicular_segments=[s[0] for s in history[2:] if s[1]==opp_axis]

    for perp_seg in perpendicular_segments:
        if isAligned(seg,perp_seg, opp_axis) and isAligned (perp_seg, seg, axis):
            return [seg[0][opp_axis],perp_seg[0][axis]]

    #impossible junction coordinate
    return [.1, .1]

#Is it possible for two segments to intersect according to the given axis
#Basically seg a has to be between seg b on the axis
def isAligned(seg_a, seg_b,axis):
    seg_b=sorted(seg_b, key=itemgetter(axis))
    return seg_a[0][axis]>=seg_b[0][axis] and seg_a[0][axis]<=seg_b[1][axis]

def updateLocation(location, distance, orient):
    x,y=location
    if orient==0:
        y+=distance
    elif orient==1:
        x+=distance
    elif orient==2:
        y-=distance
    else:
        x-=distance
    return [x,y]

def move(loc, dist, orient, dir):
    orient=updateOrientation(dir, orient)
    new_loc=updateLocation(loc, dist, orient)
    axis=getAxis(loc, new_loc)

    history.insert(0,([loc, new_loc],axis))
    loc=new_loc


def findDestination():
    bunny_plan=[]

    loc=[0,0]
    history=[]
    #facing north
    orient=0
    populatePlan(bunny_plan)

    for segment in bunny_plan:
        dir, dist=segment
        move(loc, dist, orient, dir)

        junct=findJunction(history)
        if junct!=[.1,.1]:
            print (sum(map(abs, junct))
            break

if __name__ == "__main__":
    findDestination()
