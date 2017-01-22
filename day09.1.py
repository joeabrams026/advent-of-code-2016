''' A second, less state heavy version of day 9'''

import util

def parse_marker(marker):
    return map(int, marker.split('x'))
    
def repeat(string, repeats):
    return string * repeats
    
def decompress(input):
    
    place = [0]
    decompressed = []
    
    def read(num):
        if place[0] >= len(input):
            return None
        tmp = input[place[0]:place[0]+num]
        place[0] = place[0] + num
        return tmp
    
    def read_until(end):
        l = read(1)
        if (l == end):
            return ''
        else:
            return l + read_until(end)

    while True:
        l = read(1)
        if l is None:
            break
        
        if l == '(':
            marker = read_until(')')
            mark_next_n_chars, repeats = parse_marker(marker)
            
            to_repeat = read(mark_next_n_chars)
            decompressed.extend(repeat(to_repeat, repeats))
        else:
            decompressed.append(l)

    return ''.join(decompressed)


assert decompress ('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

print len(decompress(util.Input("09").read().strip()))
