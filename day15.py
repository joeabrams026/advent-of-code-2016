
def get_done_state (maze):
	'''Unhandled edge case: when the size of capsule is greater than its index'''
	rez = []
	for i, m in enumerate(maze):
		rez.append([m[0], m[0]-(i+1)])
	return rez

def incr_time (maze):
	for i,m in enumerate(maze):
		places, cur = m
		if cur + 1 == places:
			maze[i] = ([places, 0])
		else:
			maze[i] = ([places, cur + 1]) 

	return maze


maze = [[7,0], [13,0], [3,2], [5,2], [17,0], [19,7]] # PART 1
#maze = [[7,0], [13,0], [3,2], [5,2], [17,0], [19,7],[11,0]] # PART 2
#maze = [[5,4],[2,1]] # Test
done = get_done_state(maze)

print "done state", done

for i in xrange(0,5000000):
	if done == maze:
		print "press the button at", i
		break
	incr_time(maze)


