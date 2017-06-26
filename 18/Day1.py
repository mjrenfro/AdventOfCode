#using python 3.5

import sys
import unittest
#Using the rules described by the prompt for determining traps and safe tiles
#The total number of safe tiles up to the 40th row must be determined

#Thoughts: don't need to keep track
#of all the rows.

#All that needs to be stored:
    #Running total of safe tiles
    #Previous row

#Algorithm

    #int count_safe_tiles(int max_row, string input_row){
    #
    #   sum=0
    #   current_row=0
    #while (current_row<max_row){
    #   sum+=count_safe(input_row)
    #   input_row=generate_new_row(input_row)
    #}

    #
    #}
    # print count_safe_tiles(40, input_row)
first_row = "......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^.."
trap_parents=["^^.",".^^","^..","..^"]

#assumes a row is greater than 1 tile in length
def generate_new_row(input_row):
    next_row=[]
    for idx,tile in enumerate(input_row):
        window =""
        if idx ==0:
            window="."+input_row[idx]+input_row[idx+1]
        elif idx == len(input_row)-1:
            window=input_row[idx-1]+input_row[idx]+"."
        else:
            window = input_row[idx-1]+input_row[idx]+input_row[idx+1]
        n='^' if window in trap_parents else '.'
        next_row.append(n)

    return ''.join(next_row)

def count_safe_tiles (max_row, input_row):
    sum_safe_tiles=0
    current_row=0
    while current_row<max_row:
        sum_safe_tiles+=input_row.count('.')
        input_row=generate_new_row(input_row)
        current_row+=1
    return sum_safe_tiles

class TestDay1(unittest.TestCase):
    def test_results(self):
        self.assertEqual(generate_new_row("..^^."), ".^^^^")

if __name__ == '__main__':
    #unittest.main()
    Day1 = False
    max_rows= 40 if Day1 else 400000
    print("answer ", count_safe_tiles(max_rows, first_row))
