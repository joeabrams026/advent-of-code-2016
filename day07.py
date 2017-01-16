
def is_abba(input):
    if len(input) != 4: return False
    a,b,c,d = input
    return a==d and b==c and a != b and a not in '[]' and b not in '[]'

def is_valid(input):
    in_brackets = False
    abba_found = False
    
    for i, letter in enumerate(input):
        
        if letter == '[':
            assert not in_brackets
            in_brackets = True
            continue
        if letter == ']':
            assert in_brackets
            in_brackets = False
            continue
            
        abba = is_abba(input[i:i+4])
        
        if in_brackets and abba:
            return False
            
        abba_found = abba_found or abba

    return abba_found

# Tests
print True == is_valid('abba[mnop]qrst')
print False == is_valid('abcd[bddb]xyyx')
print False == is_valid('aaaa[qwer]tyui')
print True == is_valid('ioxxoj[asdfgh]zxcvbn')

with open('day07.data', 'r') as myfile:
    print "# Valid addresses:", sum([is_valid(line.strip()) for line in myfile])
        
    


