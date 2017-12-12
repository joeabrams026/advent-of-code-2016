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
    
# part1
print "min moves to target: ", len(astar((1,1), (31,39), distance_left, possible_moves)) - 1

# part2
def possible_states(start, moves_func, max_moves):
    q = [(0, start)] # (move_count, state)
    states = {}
    
    while True:
        move_count, state = q.pop(0)
        if move_count == max_moves:
            return states
            
        for new_state in possible_moves(state):
            new_move_count = move_count+1
            if new_state not in states or new_move_count < states[new_state]:
                q.append((new_move_count, new_state ))
                states[new_state] = new_move_count
        
    

print "max states in 50 moves:", len(possible_states((1,1), possible_moves, 50))
