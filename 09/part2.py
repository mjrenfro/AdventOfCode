#inspired heavily by https://github.com/tomkooij/AdventOfCode/blob/master/aoc2016/day9.py
#Not an original solution
import re
def process_string(s):

    #necessary for sub strings that don't contain any decompression
    if ')' not in s:
        return len(s)

    left_pos=s.find('(')
    right_pos=s.find(')')

    #regex seems excessive...so split was a good idea
    length, rep=map(int, (s[left_pos+1:right_pos]).split('x'))

    curr_seg=s[right_pos+1:(length+right_pos+1)]
    next_seg=s[(length+right_pos+1):]

    return left_pos + rep*process_string(curr_seg) + process_string(next_seg)

f=open('p9input.txt')
str=f.readline().strip()
str="".join(str.split())
print (process_string(str))
