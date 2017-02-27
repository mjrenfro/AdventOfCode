import heapq
frontier=[]
key=1364

goal=(31,39)
visited=set()

#got most logic for this func from SO
def get_parity(n):
    c=0
    while n:
        c+=1
        n &= n-1
    return not bool(c%2)

#Returns the manhattan distance between two points
def find_dist(point_a, point_b):
    a_x, a_y=point_a
    b_x, b_y=point_b
    return abs(a_x-b_x) + abs(a_y-b_y)

def is_walkable(point):

    x,y=point
    if (x<0 or y<0):
        return False

    offset=x*x+3*x+2*x*y+y+y*y

    f=get_parity(offset+key)
    return f
def print_layout():
    for y in range(5):
        for x in range(8):
            if is_walkable((x,y)):
                print('.', end='')
            else:
                print('#', end='')
        print('')

#totally could use NumPy for this, but it's only a small part of
#solving the overall problem
def get_neighbors(point):
    offsets=[(0,-1), (1,0), (0,1), (-1,0)]
    neighbors=[]

    for o in offsets:
        #here is where NumPy would make this look better
        neighbors.append(tuple(sum(x) for x in zip(point, o)))
    # print (neighbors)
    return neighbors


#for determining the unique nodes at most 50 nodes away.
#Python isn't the greatest for recursive; so using a queue
#gonna steal this tuple, length idea from the amazing tomkooij :
#https://github.com/tomkooij/AdventOfCode/blob/master/aoc2016/day13.py
def breadth_first(path_head):
    queue=[path_head]
    while queue:
        dist,node=queue.pop(0)
        if node not in visited:
            visited.add(node)
            if dist ==50:
                return
            for neig in [n for n in get_neighbors(node) if is_walkable(n)]:
                queue.append((dist+1, neig))


breadth_first((0,(1,1)))
print("Num nodes < 50: ",len(visited))
