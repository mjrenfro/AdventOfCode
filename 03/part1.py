import re
import itertools

numValid=0

with open('p3input.txt') as f:
    for line in f.readlines():
        lengths=list(map(int,line.strip().split()))
        bad_triangle=False
        for pair in itertools.combinations(lengths, 2):
            if not all(i <sum(pair) for i in lengths):
                bad_triangle=True
                break
        if not bad_triangle:
            numValid+=1
    print(numValid)
