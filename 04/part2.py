import re
from collections import Counter
import operator

def shift(name, sectionId):
    offset=sectionId%26
    #one liners are impressive??...Or just very convoluted
    deciphered=[chr(max((ord(x)+offset)%(ord('z')+1),(ord('a')+offset-1-(ord('z')-ord(x))))) for x in name]
    return ''.join(deciphered)

def decrypt_name(line):
    room_name=''.join(re.findall('([a-zA-Z]+)-',line))
    id=int(re.findall('\d+',line)[0])
    return shift(room_name, id), id

with open ('p4input.txt') as f:
    for line in f.readlines():
        name, code= decrypt_name(line)
        if 'northpole' in name:
            print (code)
            break
