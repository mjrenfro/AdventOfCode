import numpy as np
import regex as re

screen=np.zeros([6,50])

def make_rect(rc):
    screen[0:rc[1], 0:rc[0]]=1

def rotate(args):
    args[1:]=list(map(int, args[1:]))
    if args[0]=="x":
        screen[:,args[1]]=np.roll(screen[:,args[1]],args[2])
        return
    screen[args[1]]=np.roll(screen[args[1]], args[2])

def update_screen(line):
    cmd=line.split()[0]
    if  cmd=="rect":
        make_rect(list(map(int,re.findall(r"(\d+)x(\d)",line)[0])))
    elif cmd=="rotate":
        rotate(list(re.findall(r"(y|x)=(\d+) by (\d+)", line)[0]))

with open ('pr8_input.txt') as f:
    for line in f.readlines():
        update_screen(line)
    print(np.sum(screen))
