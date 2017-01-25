import re

def has_ABBA(str):
    #can't get a regex to enforce uniqueness...
    results=re.findall(r"(([a-z])([^\2])\3\2)", str)
    return results!=[] and results[0][1]!=results[0][2]

def is_valid(line):
    non_hypernet=re.split("\[[a-z]+\]", line)
    hypernet=re.findall("\[([a-z]+)\]", line)
    return True in list(map(has_ABBA, non_hypernet)) and not (True in list( map (has_ABBA, hypernet)))

with open ('p7input.txt') as f:
    count =0
    for line in f.readlines():
        if is_valid(line.strip()):
            count+=1
    print(count)
