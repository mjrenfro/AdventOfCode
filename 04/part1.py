import re
from collections import Counter
import operator

def valid_id(line):
    room_name="".join(re.findall('([a-zA-Z]+)-',line))
    c=Counter(room_name)
    top_five="".join(sorted(c, key=lambda x: (-c[x],x))[:5])

    check_sum=re.findall('\[(.{5})\]', line)[0]
    id=int(re.findall('\d+',line)[0])
    return id if top_five==check_sum else 0


with open('p4input.txt') as f:
    sum=0
    for line in f.readlines():
        sum+=valid_id(line)

    print (sum)
