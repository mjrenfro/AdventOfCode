from collections import deque
import sys
import unittest


def solver(lines, password):
    password=list(password)
    for line in lines:
        words = line.split()

        #swap position X with position Y
        if "swap" in words and "position" in words:
            x,y=int(words[2]), int(words[5])
            password[x], password[y]=password[y], password[x]

        #swap letter X with letter Y
        elif "swap" in words and "letter" in words:
            x,y = password.index(words[2]), password.index(words[5])
            password[x],password[y]=password[y], password[x]

        #rotate left/right X step(s)
        elif "rotate" in words and any("step" in word for word in words):
            steps=int(words[2])
            deque_password=deque(password)
            if "left" == words[1]:
                deque_password.rotate(steps*-1)
            else:
                deque_password.rotate(steps)
            password= list(deque_password)

        #rotate based on position of letter X
        elif "rotate" in words and "position" in words:
            deque_password = deque(password)
            x = password.index(words[6])
            offset=x+1 if x<4 else x+2
            deque_password.rotate(offset)
            password=list(deque_password)

        #reverse positions X through Y
        elif "reverse" in words:
            x,y = int(words[2]), int(words[4])
            left, deque_middle, right= password[:x], deque(password[x:y+1]), password[y+1:]
            deque_middle.reverse()
            password=left+list(deque_middle)+right

        #move position X to position Y
        elif "move" in words:
            x,y=int(words[2])%len(password), int(words[5])%len(password)
            element =password.pop(x)
            password.insert(y,element)
        else:
            sys.exit("Unidentified instruction")
    return ''.join(password)

def GetLines(inputFileName):
    with open(inputFileName) as f:
        lines = [line for line in f.readlines()]
    return lines

class TestDay1(unittest.TestCase):
    def test_results(self):
        self.assertEqual(solver(GetLines("test_input.txt"),"abcde"), "decab")

if __name__ == '__main__':
    #unittest.main()
    print(solver(GetLines("input.txt"), "abcdefgh"));
