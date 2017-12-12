import re
import hashlib

salt = 'cuanljph'
#salt = 'abc'
MD5_DEPTH = 2017

def getRepeated(txt, n):
    '''returns char of first triplet or else None'''
    s = re.search(r'(.)\1{' + str(n-1) + '}',txt)
    if s is not None:
        return s.group()[0]
    else:
        return None
        
print getRepeated('abb777bbc', 3)

letter = None

md5s = {}

def md5OfStr(txt):
    if txt in md5s:
        return md5s[txt]
    
    hashed = txt
    for i in xrange(MD5_DEPTH):
        hashed = hashlib.md5(hashed).hexdigest()
        
    
    md5s[txt] = hashed
    
    return hashed

def md5(num):
    to_hash = salt + str(num)
    return md5OfStr(to_hash)
    
def getNextTriplet(start):
    while True:
        if (getRepeated(md5(start), 3)):
            return start, getRepeated(md5(start),3)
        start += 1

def getNextFiver(start, letter):
    for i in xrange(start, start + 1000):
        if (getRepeated(md5(i), 5)):
            if letter == getRepeated(md5(i),5):
                return i

start = 0
key_chars = []
while len(key_chars) < 64:
    
    triplet, letter = getNextTriplet(start)
    fiver = getNextFiver(triplet+1, letter)
    if fiver is not None:
        print triplet, fiver
        start = fiver+1
        key_chars.append(fiver)

    start = triplet + 1
