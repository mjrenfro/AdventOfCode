
def reduceMax (max_high, interval, partA=True):
        gap =interval[0]-(max_high[0]+1)
        if gap>0:
            interval[0]=gap
            interval[1]=max_high[0]+1
            if not partA: max_high[0]=max(max_high[0], interval[1])
            return True

        max_high[0]=max(max_high[0], interval[1])


def solver(ranges, partA=True):
    max_high=[0]
    result=[x[1] if partA else x[0] for x in ranges if reduceMax(max_high, x, partA) ]
    return result[0] if partA else sum(result)


with open('input.txt') as f:
    ranges = sorted([list(map(int,line.split('-'))) for line in f.readlines()])

print(solver(ranges, True))
