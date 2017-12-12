from bitarray import bitarray

def dragonize(a):
	b = a.copy()
	b.reverse()
	b.invert()

	a.append(False)
	a.extend(b)
	return a

def randomize(a, desired_len):
	while a.length() < desired_len:
		a = dragonize(a)

	return a[:desired_len]

def checksum(a):

	orig = a
	chk_arr = bitarray()

	while chk_arr.length() % 2 == 0:
		chk_arr = bitarray()

		for idx in xrange(len(orig)/2):
			i,j = orig[idx*2:idx*2 + 2]
			chk_arr.append(i == j)

		orig = chk_arr

	return chk_arr


print "Tests:"
print dragonize(bitarray('1')) == bitarray('100')
print dragonize(bitarray('0')) == bitarray('001')
print dragonize(bitarray('11111')) == bitarray('11111000000')
print dragonize(bitarray('111100001010')) == bitarray('1111000010100101011110000')

print randomize(bitarray('10000'), 20) == bitarray('10000011110010000111')

print "test 1", checksum(randomize(bitarray('10000'), 20))
print "part 1", checksum(randomize(bitarray('01111010110010011'), 272))
print "part 2", checksum(randomize(bitarray('01111010110010011'), 35651584))