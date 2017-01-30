#Split into data assignment and instructions
#Not memory efficient, but the input is so small that
#loading all the text into lists shouldn't be an issue
#not original
from collections import defaultdict
bots =defaultdict(list)
output=defaultdict(list)
target=[17,61]

def process(line):

    type, *args= line.split()
    if type=='value':
        bots[int(args[4])].append(int(args[0]))
        return True
    else:
        return process_instructions(args)

#bot 129 gives low to bot 52 and high to bot 57
def process_instructions(args):
    curr_bot=int(args[0])
    if len(bots[curr_bot]) != 2:
        return False

    mi=min(bots[curr_bot])
    ma=max(bots[curr_bot])
    if args[4]=='bot':
        bots[int(args[5])].append(mi)
    else:
        output[int(args[5])]=mi
    if args[9]=='bot':
        bots[int(args[10])].append(ma)
    else:
        output[int(args[10])]=ma
    return True

with open('input.txt') as f:
    lines= [l.strip() for l in f.readlines()]
    while lines:
        for l in lines:
            if process(l):
                lines.remove(l)

for key, value in bots.items():
    if target== sorted(value):
        print("Bot ",key)
