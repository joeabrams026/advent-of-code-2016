import re

def parse(line):
    match = re.match('([a-z-]+)([0-9]+)\[([a-z]+)\]', line)
    if not match:
        print "WARNING: parse failed for line ", line
    else:
        encrypted, sector, checksum = match.groups()
        return encrypted, int(sector), checksum
        
def get_checksum(encrypted):
    counter = {letter:0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

    for letter in encrypted:
        if letter is not '-':
            counter[letter] = counter[letter] + 1

    non_zeros = [c for c in counter.iteritems() if c[1] > 0]
    top_sorted_counts = sorted(non_zeros, key=lambda c: (-c[1], c[0]))[:5]
    
    return ''.join([l[0] for l in top_sorted_counts])

print ("Tests:", get_checksum(parse('aaaaa-bbb-z-y-x-123[abxyz]')[0]) == 'abxyz',
    get_checksum(parse('a-b-c-d-e-f-g-h-987[abcde]')[0]) == 'abcde')

running_total = 0
with open('day04.data', 'r') as myfile:
    for line in myfile:
        line = line.strip()
        encrypted, sector, checksum = parse(line)
        real_checksum = get_checksum(encrypted)
        if real_checksum == checksum:
            running_total += sector
        
print "Running total:", running_total
