'''A very stateful first attempt at day9.  Works, but ugh'''
import util

def parse_marker(marker):
    mark_next_n_chars, repeats = marker.split('x')
    return int(mark_next_n_chars), int(repeats)
    
def repeat(string, repeats):
    return string * repeats

def decompress(input):
    
    in_marker = False
    marker = ''
    decompressed = ''
    mark_next_n_chars, repeats = 0, 0
    marked_chars = ''
    
    for i,letter in enumerate(input):
        if letter == '(' and mark_next_n_chars <= 0:
            assert not in_marker
            in_marker = True

        elif letter == ')' and mark_next_n_chars <= 0:
            assert in_marker
            in_marker = False
            mark_next_n_chars, repeats = parse_marker(marker)
            marker = ''

        elif in_marker:
            marker += letter
        
        elif mark_next_n_chars > 0:
            marked_chars += letter
            mark_next_n_chars -= 1
            
            if marked_chars != '' and mark_next_n_chars == 0:
                decompressed += repeat(marked_chars, repeats)
                repeats = 0
                marked_chars = ''
        else:
            decompressed += letter

    return decompressed
        
assert decompress ('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

print len(decompress(util.Input("09").read().strip()))
