import re
from collections import Counter
import operator

filename='p4input.txt'
#filename='p4sample.txt'
inputRooms=open(filename)
sumIds=0

def readInRoom():
    global inputRooms
    nextRoom=inputRooms.readline().rstrip()
    if nextRoom=="":
        return -1
    return nextRoom

#part 2
def extractName(room):
    roomInfo=[]

    regex=re.compile('^(.*?)\d+')
    rawName=regex.findall(room)[0]
    explodedName=re.findall("[a-zA-Z]+", rawName)
    roomInfo.append(explodedName)

    sectionId=re.compile('\d+')
    roomInfo.append(int(sectionId.findall(room)[0]))

    return roomInfo

def shift(name, sectionId):
    offset=sectionId%26
    deciphered=[chr(max((ord(x)+offset)%(ord('z')+1),(ord('a')+offset-1-(ord('z')-ord(x))))) for x in name]
    return ''.join(deciphered)




def shiftName(roomInfo):
    explodedName=roomInfo[0]
    sectionId=roomInfo[1]
    for idx,name in enumerate(explodedName):        
        explodedName[idx]=shift(name, sectionId)
    print(explodedName)
    print(sectionId)




#part 1
def splitRoom(room):
    roomInfo=[]

    #get the room name
    bigName=re.compile('^(.*?)\d+')
    bN=bigName.findall(room)[0]
    sN="".join(re.findall("[a-zA-Z]+", bN))
    myCount=Counter(sN)
    mc_list=myCount.most_common(len(sN))
    temp=sorted(mc_list, key=operator.itemgetter(0))
    tempA=sorted(temp, key=operator.itemgetter(1), reverse=True)
    tempA=tempA[:5]
    top_letters=[x[0] for x in tempA]
    top_string="".join(top_letters)
    roomInfo.append(top_string)



    #get the room section ID
    sectionId=re.compile('\d+')
    roomInfo.append(int(sectionId.findall(room)[0]))

    #get the checksum
    checkSum_re=re.compile('\[(.{5})\]')
    checkSum=checkSum_re.findall(room)[0]
    roomInfo.append(checkSum)

    return roomInfo

def validRoom(roomInfo):
    return roomInfo[2]==roomInfo[0]
#part 2
def processCypher():
    new_room=readInRoom()
    while new_room!=-1:
        ri=extractName(new_room)
        shiftName(ri)
        new_room=readInRoom()

#part 1
def processRooms():
    global sumIds
    new_room=readInRoom()
    while new_room!= -1:
        ri=splitRoom(new_room)
        if validRoom(ri):
            sumIds+=ri[1]
        new_room=readInRoom()

if __name__ == "__main__":
    processCypher()
    #print(sumIds)
