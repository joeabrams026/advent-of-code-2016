'''Brute force approach to day 11.  Works and takes about 2 min.'''

import copy
import datetime
from heapq import heappush, heappop
from itertools import combinations
from collections import deque

board = [{'sg','sm','pg','pm'}, {'tg','rg','rm','cg','cm'}, {'tm'}, set()]
goal = [set(), set(), set(), {'sg','sm','pg','pm','tg','rg','rm','cg','cm','tm'}]

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
    for items in combinations(floor,1):
        make_new_board(items)

    # all combos of "2"
    for items in combinations(floor, 2):
        make_new_board(items)
        
    return new_boards

def solve(board, goal):
    queue = deque()
    in_queue = set()
    
    def add_to_queue(elevator_floor_num, move_count, boards):
        for board in boards:
            board_hash = get_board_hash(board, elevator_floor_num)
            if board_hash not in in_queue:
                in_queue.add(board_hash)
                queue.append((board, elevator_floor_num, move_count))
                

    add_to_queue(0, 0, [board])
    
    for i in range(10000000): # prevent endless loop when debugging
        board, elevator_floor_num, move_count = queue.popleft()
        if board == goal:
            print "solved in %s " % (move_count)
            get_board_hash(board, elevator_floor_num), move_count
            return move_count
            
        if i % 10000 == 0: # Some progress updates
            print "%s - board: %s, move_count: %s " % (datetime.datetime.utcnow(), get_board_hash(board, elevator_floor_num), move_count)

        # elevator up boards
        if elevator_floor_num in (0,1,2):
            new_boards = get_moves(board,elevator_floor_num,1)
            add_to_queue(elevator_floor_num+1, move_count +1, new_boards)

        # elevator down boards
        if elevator_floor_num in (1,2,3):
            new_boards = get_moves(board,elevator_floor_num,-1)
            add_to_queue(elevator_floor_num-1, move_count +1, new_boards)

print solve(board,goal)



