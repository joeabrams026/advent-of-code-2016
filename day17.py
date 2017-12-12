'''
- 4x4 grid.  
- start top left, end bottom right
- given position in the maze, find md5 hash of input + UDLR sequence to where you are
- look at first 4 letters of hash to get status of UDLR posibilities
	- [bcdef] means door is open
'''

import hashlib
input = 'njfxhljp'
#input = 'ihgpwlah' # sample 1
#input = 'kglvqrro' # sample 2
#input = 'ulqzkmiv' # sample 3
opens = 'bcdef'
input_len = len(input)


def is_done(input):
	U,D,L,R = get_counts(input)
	return D - U == 3 and R - L == 3

def get_counts(input):
	U, L, R, D = 0,0,0,0
	for c in input:
		if c == 'U': U += 1
		if c == 'L': L += 1
		if c == 'D': D += 1
		if c == 'R': R +=1
	return U,D,L, R

def is_inbounds(input):
	U,D,L,R = get_counts(input)

	return D-U < 4 and U-D <= 0 and L-R <= 0 and R-L < 4

def get_moves(input):
	moves = []

	md5 = hashlib.md5()
	md5.update(input)
	doors = md5.hexdigest()[:4]

	if doors[0] in opens: moves.append('U')
	if doors[1] in opens: moves.append('D')
	if doors[2] in opens: moves.append('L')
	if doors[3] in opens: moves.append('R')

	return moves


stack = [input]

print is_inbounds('U') == False
print is_inbounds('L') == False
print is_inbounds('R') == True
print is_inbounds('D') == True
print is_inbounds('DDDD') == False
print is_inbounds('RRRR') == False

tested = set()
dones = set()
while len(stack) > 0:
	cur = stack.pop(0)

	if is_done(cur):
		dones.add(cur)
		continue

	tested.add(cur)

	for move in get_moves(cur):
		next = cur + move

		if next not in tested and is_inbounds(next):
			stack.append(next)


print "shortest path", min(dones, key=len) [input_len:]
print "longest path", len(max(dones, key=len)) - input_len
