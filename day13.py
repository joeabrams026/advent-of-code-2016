from heapq import heappush, heappop
from math import sqrt

def onesInNSlow(n):
    mod = n % 2
    if n/2 == 0:
        return mod
    else:
        return mod + onesInN(n/2)
        
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
    #fave=10
    total = (x*x + 3*x + 2*x*y + y + y*y) + fave
    return (onesInN(total) % 2 == 1)
    
def path(s, prevs):
    return ([] if (s is None) else path(prevs[s], prevs) + [s])
    
def moves(xy):
    x,y = xy
    return (coord for coord in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) if coord[0] >= 0 and coord[1] >=0 and not isWall(coord))

def heuristic(xy,goalxy):
    x1,y1 = xy
    x2,y2 = goalxy
    return abs(x1-x2) + abs(y1-y2)

def solve(goalxy):
    goalx,goaly = goalxy
    prevs = {}
    move_counts = {} # state : moves_to_state
    q = []
    
    def add(xy,prev, move_count):
        if not xy in move_counts or move_count <= move_counts[xy]:
            x,y = xy
            heappush(q,(heuristic(xy,goalxy)+move_count, xy, move_count))
            prevs[xy] = prev
            move_counts[xy] = move_count
            
    add((1,1),None,0)
    
    while len(q) > 0:
        popped = heappop(q)
        _, xy,move_count = popped
        x,y = xy
        if x == goalx and y == goaly:
            return path(xy,prevs)
            
        for move in moves(xy):
            add(move, xy, move_count+1)
            
    
print len(solve((31,39))) - 1
#print solve((7,4))
#print solve((2,2))