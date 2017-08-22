def dragonize(a):
	b = []
	for bit in a[::-1]:
		if bit == '1':
			b.append('0')
		else:
			b.append('1')
	return a + '0' + ''.join(b)

def randomize(a, desired_len):
	while len(a) < desired_len:
		a = dragonize(a)

	return a[:desired_len]

def even(a):
	return len(a) % 2

def checksum(a):

	orig = list(a)

	for z in xrange(100):
		chk_arr = []

		for idx in xrange(len(orig)/2):
			i,j = orig[idx*2:idx*2 + 2]
			if i == j:
				chk_arr.append('1')
			else:
				chk_arr.append('0')


		if len(chk_arr) % 2 == 1:
			return ''.join(chk_arr)

		orig = chk_arr


print "Tests:"
print dragonize('1') == '100'
print dragonize('0') == '001'
print dragonize('11111') == '11111000000'
print dragonize('111100001010') == '1111000010100101011110000'

print randomize('10000', 20) == '10000011110010000111'

print checksum(randomize('10000', 20))
print checksum(randomize('01111010110010011', 35651584))