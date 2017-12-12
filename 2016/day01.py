def parse_path (raw_input):
    return map(lambda x: x.strip(),  raw_input.split(",") )

def go_left (cur_direction):
    return {"N":"E", "E":"S", "S":"W", "W":"N"}[cur_direction]

def go_right (cur_direction):
    return {"N":"W", "W":"S", "S":"E", "E":"N"}[cur_direction]
    
def new_direction(left_or_right, cur_direction):
    if left_or_right == "L":
        return go_left(cur_direction)
    elif left_or_right == "R":
        return go_right(cur_direction)
        
def calc_dist(nesw):
    return (abs(nesw["N"]- nesw["S"]) + abs(nesw["E"]- nesw["W"]))
    
def parse(move):
    return move[0], int(move[1:])
    
def update(nesw, direction, dist):
    nesw[direction] += dist
    
def calc (raw_input):
    nesw = {"N":0, "E":0, "S":0, "W":0}
    cur_direction = "N"
    path = parse_path(raw_input)

    for move in path:
        left_or_right, dist = parse(move)
        cur_direction = new_direction(left_or_right, cur_direction)
        update(nesw, cur_direction, dist)
    
    print nesw, calc_dist(nesw)
    

print calc ("L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4")
