#solution for both day and 2. The only difference between the days is the goal input
import copy

def fill_disk(data, goal):
    while True:
        a = data
        b=copy.deepcopy(a)
        b.reverse()
        data=a+[0]+[x^1 for x in b]
        if len(data)>=goal:
            return data[:goal]


def calc_checksum(data):
    pairs=list(zip(data, data[1:]))[::2]
    return [1 if p[0]==p[1] else 0 for p in pairs]

def solver(input,goal):


    gen_data=fill_disk(input,goal)

    checksum=calc_checksum(gen_data)
    while len(checksum)%2==0:
        checksum=calc_checksum(checksum)
    return checksum

solution=solver([int(x) for x in list ("10011111011011001")],35651584)
print ("checksum: ", ''.join(str(x )for x in solution))
