import copy
encoded_digits=[]
decoded_digits=[]
position=[0,0] #=5

keypad_coor=[(0,0), (1,-1), (1,0), (1,1), (2,-2), (2,-1), (2,0), (2,1), (2,2), (3,-1), (3,0), (3,1), (4,0)]
keypad_val=['5', 'A', '6', '2', 'D', 'B', '7', '3', '1', 'C', '8', '4', '9']


def readInEncoding():
    global encoded_digits
    #read in file and put each line as an element in ED
    with open("p2Input.txt") as f:
        content=f.readlines()
    encoded_digits = [x.strip() for x in content]

#Try to step to the new grid cell if on keypad
def decode(direction):
    global position
    new_pos=copy.copy(position)
    step(direction, new_pos)
    if tuple(new_pos) in keypad_coor:
        position=new_pos

#Update position one step in the given direction
def step(direction, pos):
    if direction=='U':
        pos[1]+=1
    elif direction=='L':
        pos[0]-=1
    elif direction=='R':
        pos[0]+=1
    elif direction=='D':
        pos[1]-=1

#Find the digit at the coordinate and add it to the password
def updateDecodedDigits():
    global decoded_digits
    decoded_digits+=keypad_val[keypad_coor.index(tuple(position))]

#Decode all lines in the file
def processDecoding():
    for line in encoded_digits:
        for a in line:
            decode(a)
        updateDecodedDigits()


if __name__ == "__main__":
    readInEncoding()
    processDecoding()
    print (''.join(decoded_digits))
