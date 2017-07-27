from collections import deque
import sys
import unittest

#swaps two elements in place
def swap(array, pos1, pos2):
    array[pos1],array[pos2]= array[pos2], array[pos1]

def rotate(array, steps):
    #using deque because has the easiest rotate method to use
    deque_array=deque(array)
    deque_array.rotate(steps)
    return list(deque_array)

def move(array, pos1, pos2):
    element=array.pop(pos1)
    array.insert(pos2, element)

def solver(lines, password, scramble=True):
    password=list(password)
    if not scramble: lines=list(reversed(lines))

    for line in lines:
        words = line.split()

        #swap position X with position Y
        if "swap" in words and "position" in words:
            x,y=int(words[2]), int(words[5])
            swap(password,x,y)

        #swap letter X with letter Y
        elif "swap" in words and "letter" in words:
            x,y = password.index(words[2]), password.index(words[5])
            swap(password,x,y)

        #rotate left/right X step(s)
        elif "rotate" in words and any("step" in word for word in words):
            steps=int(words[2])
            direction = 1 if scramble else -1

            if "left" == words[1]:
                password=rotate(password, direction*steps*-1)
            else:
                password=rotate(password, direction*steps)

        #rotate based on position of letter X
        elif "rotate" in words and "position" in words:
            position = password.index(words[6])

            #mapping between new position and former position
            #Know that the length of the password is 8 and wrap arounds
            unscrambler_map={1:0, 3:1, 5:2, 7:3, 2:4, 4:5, 6:6, 0:7}

            steps = (position+1 if position<4 else position+2) if scramble else unscrambler_map[position]-position
            password=rotate(password,steps)

        #reverse positions X through Y
        elif "reverse" in words:
            x,y = int(words[2]), int(words[4])
            password=password[:x] +list(reversed(password[x:y+1]))+ password[y+1:]

        #move position X to position Y
        elif "move" in words:
            x,y=int(words[2])%len(password), int(words[5])%len(password)
            if scramble: move(password, x,y)
            else: move(password, y,x)

        #used mostly for debuging of instruction interpretation
        else:
            sys.exit("Unidentified instruction")
    return ''.join(password)

def GetLines(inputFileName):
    with open(inputFileName) as f:
        lines = [line for line in f.readlines()]
    return lines

class TestSolution(unittest.TestCase):
    def test(self):
        with self.subTest(scramble=True):
            self.assertEqual(solver(GetLines("test_input.txt"),"abcde"), "decab")

        #CANNOT test unscrambling completely on a password with length 5 because there isn't
        #a one-to-one unscrambling map

        # with self.subTest(scramble=False):
        #     self.assertEqual(solver(GetLines("test_input.txt"), "ecabd", False), "abcde")

if __name__ == '__main__':
    #unittest.main()
    print(solver(GetLines("input.txt"), "fbgdceah", False));
