import re
import util
from collections import defaultdict

def solve(instructions):
    bot_hands = defaultdict(list)
    re_assgn = re.compile(r'value (\d+) goes to (bot \d+)').match
    re_hi_lo = re.compile(r'(bot \d+) gives low to ([a-z]+ \d+) and high to ([a-z]+ \d+)').match
    rules = [] #giver, lowReceiver, highReciever
    
    def hands_full(giver):
        return len(bot_hands[giver]) == 2
        
    def give(val, giver, receiver):
        bot_hands[giver].remove(val)
        bot_hands[receiver].append(val)
    
    def hand_for(giver):
        return bot_hands[giver]
    
    # setup
    for inst in instructions:
        assgn = re_assgn(inst)
        hi_lo = re_hi_lo(inst)
        
        if assgn:
            value, bot = assgn.groups()
            bot_hands[bot].append(int(value))
        elif hi_lo:
            rules.append(hi_lo.groups())
        else:
            assert false
    
    while rules:
        
        rule = rules.pop(0)
        giver, lowReceiver, highReciever = rule
        
        if hands_full(giver):
            low, high = sorted (hand_for(giver))
            if (low, high) == (17,61):
                print "giver: %s low: %s high: %s" % (giver, low, high)
            give(low, giver, lowReceiver)
            give(high, giver, highReciever)
        else:
            rules.append(rule)
                
    return bot_hands
    
print solve('''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''.strip().split('\n'))

instructions = util.Input("10").read().strip().split('\n')
print solve(instructions)
            
        
        
