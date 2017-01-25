import regex as re

def has_ABA(str):
    #can't get a regex to enforce uniqueness...
    if (re.findall(r"(([a-z])([^\2])\2)", str)) !=[]:
        return [x[0] for x in (re.findall(r"(([a-z])([^\2])\2)", str, overlapped=True))]
    return []

def invert(aba):
    return aba[1]+aba[0]+aba[1]
def is_valid(line):
    bundle=[re.split("\[[a-z]+\]", line),re.findall("\[([a-z]+)\]", line)]

    #clean up if possible with list comprehensions, maps
    ABAs=[[],[]]
    for idx, b in enumerate(bundle):
        for seg in b:
            ABAs[idx].extend(has_ABA(seg))
    return [ABA for ABA in ABAs[0] if invert(ABA) in ABAs[1]]!=[]

with open ('p7input.txt') as f:
    count =0
    for line in f.readlines():
        if is_valid(line.strip()):
            count+=1
    print(count)
