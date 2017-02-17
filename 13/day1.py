import heapq
frontier=[]
key=1364

goal=(31,39)

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
    return get_parity(offset+key)

#totally could use NumPy for this, but it's only a small part of
#solving the overall problem
def get_neighbors(point):
    offsets=[(0,-1), (1,0), (0,1), (-1,0)]
    neighbors=[]

    for o in offsets:
        #here is where NumPy would make this look better
        neighbors.append(tuple(sum(x) for x in zip(point, o)))

    return neighbors

def a_star():
    start=(1,1)
    heapq.heappush(frontier, (0,(1,1)) )
    came_from={}
    cost_so_far={}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier==[]:
        print (cost_so_far)
        current=heapq.heappop(frontier)[1]
        print (current)

        if current==goal:
            print ("Cost so far ", cost_so_far)
            return cost_so_far[current]

        for neig in [n for n in get_neighbors(current) if is_walkable(n)]:
            print("neig: ", neig)
            new_cost=cost_so_far[current] + 1
            if neig not in cost_so_far or new_cost<cost_so_far[neig]:
                cost_so_far[neig]=new_cost
                priority=new_cost+find_dist(goal, neig)
                heapq.heappush(frontier, (priority,neig) )
                came_from[neig]=current
print(a_star())
