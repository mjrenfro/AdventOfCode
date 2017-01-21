#heavily influenced by https://github.com/tomkooij/AdventOfCode/blob/master/aoc2016/day1.pyc
#https://github.com/godarderik/adventofcode/blob/master/2016/problem2.py

encoded_digits=[]
decoded_digits=[]
x,y=0,0 #=5

keypad_coor={(0,0):'5',(1,-1):'A',(1,0):'6',(1,1):'2',(2,-2):'D',(2,-1):'B',(2,0):'7',(2,1):'3',(2,2):'1', (3,-1):'C', (3,0):'8', (3,1):'4', (4,0):'9'}

#just need a single map, no need to cross reference
update_position={'U':lambda x,y: (x,y+1),
                 'D':lambda x,y: (x,y-1),
                 'R':lambda x,y: (x+1,y),
                 'L':lambda x,y: (x-1,y)}

with open('p2Input.txt') as f:
    for line in f.readlines():
        for dir in line.strip():
            coord=update_position[dir](x,y)
            if coord in keypad_coor:
                x,y =coord
        print(keypad_coor[(x,y)], end="")
    print()
