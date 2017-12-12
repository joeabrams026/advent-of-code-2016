''' some utils mostly borrowed from Norvig http://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb'''
from heapq import heappush, heappop

def Input(day):
    "Open this day's input file."
    filename = 'day{}.data'.format(day)
    return open(filename)
    
    
def path(s, prevs):
    return ([] if (s is None) else path(prevs[s], prevs) + [s])
    
def astar(start_state, goal_state, heuristic, new_states):

    prevs = {}
    move_counts = {} # state : moves_to_state
    q = []
    
    def add(state,prev, move_count):
        if not state in move_counts or move_count <= move_counts[state]:
            heappush(q,(heuristic(state,goal_state)+move_count, state, move_count))
            prevs[state] = prev
            move_counts[state] = move_count
            
    add(start_state,None,0)
    
    while len(q) > 0:
        popped = heappop(q)
        _, state, move_count = popped
        
        if heuristic(state,goal_state) == 0:
            return path(state,prevs)
            
        for move in new_states(state):
            add(move, state, move_count+1)
            
    
    
