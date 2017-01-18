#Problem description can be found @ https://adventofcode.com/2016/day/1

#Approach:
#Split each segment in the list of moves into its direction and distance
#Have 2 state variables describing the spy to keep track of the currect location and direction
#Update the spy's state until all segments have been processed

import re

plan_input="L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"

#Reorganizes the input so that each 'segment' is a 2D list
def populatePlan(plan):
    for inst in re.split(', ', plan_input):
        plan.append([inst[:1], int(inst[1:])])


def updateDirection(instr, direction):
    if instr[0]=='L':
        direction[0]=(direction[0]-1)%4
    else:
        direction[0]=(direction[0]+1)%4

#Move the spy according to the segment's info
def updateLocation(location, distance, direction):
    dir=direction[0]
    #north
    if dir==0:
        location[1]+=distance
    #east
    elif dir==1:
        location[0]+=distance
    #south
    elif dir==2:
        location[1]-=distance
    #west
    else:
        location[0]-=distance

def findDestination():
    #Easter bunny headquarters plan
    bunny_plan=[]

    #face north
    spy_direction=[0]

    location=[0,0]
    populatePlan(bunny_plan)

    for segment in bunny_plan:
        updateDirection(segment[0], spy_direction)
        updateLocation(location,segment[1],spy_direction)

    print (abs(location[0])+abs(location[1]))

if __name__ == "__main__":
    findDestination()
