'''Brute force approach to day 11.  Works and takes about 2 min.'''

import copy
import datetime
import math
from heapq import heappush, heappop
from itertools import combinations
from collections import deque

def get_board_hash(board, elevator_floor_num):
    return '_'.join([''.join(sorted(floor)) for floor in board]) + '_' + str(elevator_floor_num)

def is_valid_board(board):
    for floor in board:
        generators = set()
        micros = set()
        
        for item in floor:
            if item[1] == 'g':
                generators.add(item[0])
            if item[1] == 'm':
                micros.add(item[0])
                
        if not generators:
            continue
        
        if micros - generators:
            return False
    
    return True
    
print True == is_valid_board([{'sg','sm','pg','pm'}, {'tg','rg','rm','cg','cm'}, {'tm'}, {}])
print False == is_valid_board([{'sm','pg','pm'}])
print True == is_valid_board([{'sm','pm'}])
print True == is_valid_board([{'pg'}])
print True == is_valid_board([{'pm'}])

# Get the legal moves given board, elevator floor, and elevator direction
def get_moves(board, elevator_floor_num, elevator_direction):
    new_boards = [] # [(elevator_floor_num, board)]
    floor = board[elevator_floor_num]
    new_floor_num = elevator_floor_num + elevator_direction

    def make_new_board (items):
        new_board = copy.deepcopy(board)
        floor_copy = new_board[elevator_floor_num]
        new_floor = new_board[new_floor_num]
        
        for item in items:
            floor_copy.discard(item)
            new_floor.add(item)

        if is_valid_board(new_board):
            new_boards.append(new_board)

    # all combos of "1"
    for items in combinations(floor, 1):
        make_new_board(items)

    # all combos of "2"
    for items in combinations(floor, 2):
        make_new_board(items)
        
    return new_boards
    
# heuristic.  0 when all pieces at the top.
def calc_heur(board):
    floor_count = len(board)
    total = 0
    for i,floor in enumerate(board):
        total += (floor_count - (i+1)) * len(floor)
        
    return math.ceil(total/2) # divide by 2 since 2 peices can be moved at once
    
def Path(previous, s): 
    "Return a list of states that lead to state s, according to the previous dict."
    return ([] if (s is None) else Path(previous, previous[s]) + [s])

def solve(board, goal):
    queue = []
    in_queue = {} # hash : moves
    prevs = {}
    
    def add_to_queue(elevator_floor_num, move_count, board, prev_hash):
        board_hash = get_board_hash(board, elevator_floor_num)
        
        if board_hash not in in_queue or move_count < in_queue[board_hash]:
            in_queue[board_hash] = move_count
            heuristic = calc_heur(board)
            heappush(queue, (heuristic + move_count, board, elevator_floor_num, move_count))
            prevs[board_hash] = prev_hash
                
    add_to_queue(0, 0, board, None)
    
    for i in range(10000000): # prevent endless loop when debugging
        heuristic, board, elevator_floor_num, move_count = heappop(queue)
        if board == goal:
            print "solved in %s " % (move_count)
            board_hash = get_board_hash(board, elevator_floor_num)
            path = Path(prevs, board_hash)
            print len(path) - 1
            return move_count
            
        if i % 10000 == 0: # Some progress updates
            print "%s - board: %s, move_count: %s " % (datetime.datetime.utcnow(), get_board_hash(board, elevator_floor_num), move_count)

        current_hash = get_board_hash(board, elevator_floor_num)
        
        for floor_change in (-1, 1):
            new_floor_num = floor_change + elevator_floor_num
            if new_floor_num in {0,1,2,3}:
                new_boards = get_moves(board, elevator_floor_num, floor_change)
                for new_board in new_boards:
                    add_to_queue(new_floor_num, move_count+1, new_board, current_hash)

board = [{'sg','sm'}, set(), set(), {'pg','pm','tg','rg','rm','cg','cm','tm'}]
goal = [set(), set(), set(), {'sg','sm','pg','pm','tg','rg','rm','cg','cm','tm'}]
solve(board,goal) # 3 moves

board = [{'sm'}, set(), set(), {'sg','pg','pm','tg','rg','rm','cg','cm','tm'}]
goal = [set(), set(), set(), {'sg','sm','pg','pm','tg','rg','rm','cg','cm','tm'}]
solve(board,goal) # 3 moves

board = [{'sg','sm','pg','pm'}, {'tg','rg','rm','cg','cm'}, {'tm'}, set()] #Part 1
goal = [set(), set(), set(), {'sg','sm','pg','pm','tg','rg','rm','cg','cm','tm'}]
#solve(board,goal)

# part 2
board = [{'eg','em','sg','sm','pg','pm','dg','dm'}, {'tg','rg','rm','cg','cm'}, {'tm'}, set()]
goal = [set(), set(), set(), {'sg','sm','pg','pm','tg','rg','rm','cg','cm','tm','eg','em','dg','dm'}]

solve(board,goal)