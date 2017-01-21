#heavily influenced by https://github.com/tomkooij/AdventOfCode/blob/master/aoc2016/day1.pyc
#https://github.com/godarderik/adventofcode/blob/master/2016/problem2.py
x,y=1,1
keypad=['741','852','963']

#just need a single map, no need to cross reference
update_position={'U':lambda x,y: (x,y+1),
                 'D':lambda x,y: (x,y-1),
                 'R':lambda x,y: (x+1,y),
                 'L':lambda x,y: (x-1,y)}

with open('p2Input.txt') as f:
    for line in f.readlines():
        for dir in line.strip():
            coord=update_position[dir](x,y)
            if any(t<0 or t>2 for t in coord):
                continue
            x,y=coord
        print(keypad[x][y], end="")
    print()
