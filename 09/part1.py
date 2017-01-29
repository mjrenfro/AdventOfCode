#A messy non recursive solution
import re

count=0

def jump_ahead(f):
    global count
    str=""
    ch=f.read(1)
    while ch!=")":
        str+=ch
        ch=f.read(1)
    len, rep=map( int, list(re.findall(r"(\d+)x(\d+)",str)[0]))
    t_count =0
    while t_count<len:
        if(f.read(1)!=" "):
            t_count+=1
    count+=len*rep

with open ("p9input.txt") as f:
    while True:
        ch=f.read(1)
        if not ch: break
        if ch == " " or ch=="\n":
            continue
        if ch =="(":
            jump_ahead(f)
            continue
        count+=1
    print (count)
