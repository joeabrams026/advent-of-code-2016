import numpy

MAX_ROW = 6
MAX_COL = 50

def clear():
    return numpy.zeros((MAX_ROW, MAX_COL))

def count_lit(board):
    return sum([sum(row) for row in board])
    
def get_char(is_set):
    if is_set: 
        return '#'
    else:
        return '.'
    
def print_board(board):
    for line in board:
        print ''.join([get_char(is_set) for is_set in line])
        
def translate(olds, ammount):
    news = [False for _ in olds]
    for i,cur_state in enumerate(olds):
        translation_row = (i + ammount) % len(news)
        news[translation_row] = cur_state
    return news
        
def transform(board, instruction):
    parsed = instruction.split()
    
    # e.g. 'rect 35x1'
    if parsed[0] == 'rect':
        x,y = parsed[1].split('x')
        right, down = int(x), int(y)
        for row in range(down):
            for col in range(right):
                board[row][col] = True

    # e.g. 'rotate row y=0 by 1'
    if parsed[0] == 'rotate':
        row_or_col = parsed[1]
        row_col_index = int(parsed[2].split('=')[1])
        ammount = int(parsed[4])
        
        if row_or_col == 'column':
            col = row_col_index
            olds = [board[row,col] for row in range(MAX_ROW)]
            news = translate(olds, ammount)
                
            for row, val in enumerate(news):
                board[row, col] = val
                
        if row_or_col == 'row':
            row = row_col_index
            olds = [board[row,col] for col in range(MAX_COL)]
            news = translate(olds, ammount)
            
            for col, val in enumerate(news):
                board[row, col] = val

    return board
    
print count_lit(clear()) == 0

print count_lit(transform(clear(), 'rect 35x2')) == 70
print print_board(transform(transform(clear(), 'rect 3x2'), 'rotate row y=1 by 16'))
print print_board(transform(transform(clear(), 'rect 3x2'), 'rotate column x=1 by 1'))

board = clear()
with open('day08.data', 'r') as myfile:
    for i, line in enumerate(myfile):
        print line
        board = transform(board, line.strip())
        print_board(board)

    print "lit count:", count_lit(board)



