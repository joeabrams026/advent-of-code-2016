from util import astar
        
def onesInN(n):
    total = 0
    while n > 0:
        total += n & 1
        n = n >> 1
    return total
    
assert onesInN(0) == 0
assert onesInN(1) == 1
assert onesInN(2) == 1
assert onesInN(3) == 2

def isWall(xy):
    x,y = xy
    fave = 1362
    total = (x*x + 3*x + 2*x*y + y + y*y) + fave
    return (onesInN(total) % 2 == 1)
    
def possible_moves(xy):
    x,y = xy
    return (coord for coord in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) 
        if coord[0] >= 0 and coord[1] >=0 and not isWall(coord))

def distance_left(xy,goalxy):
    x1,y1 = xy
    x2,y2 = goalxy
    return abs(x1-x2) + abs(y1-y2)
    
print len(astar((1,1), (31,39), distance_left, possible_moves)) - 1