def solve(problem):
	print(problem)

	patterns, encoded = problem.split(" | ")

	patterns = patterns.split()
	encoded = encoded.split()

	def pattern_to_bits(p):
		b = 0
		for c in p:
			b |= 1 << (ord(c) - ord('a'))
		return b

	def find_len(l):
		p = next(filter(lambda p: len(p) == l, patterns))
		patterns.remove(p)
		return pattern_to_bits(p)

	pat_1 = find_len(2)
	pat_7 = find_len(3)
	pat_4 = find_len(4)

	seg = [None] * 7

	seg[0] = pat_1 ^ pat_7
	seg2_set = pat_1 & pat_7
	seg1_set = pat_4 ^ seg2_set
	seg4_set = 127 ^ (seg[0] | seg1_set | seg2_set)

	for p in patterns:
		if len(p) == 5:
			b = pattern_to_bits(p)
			if b & seg2_set != seg2_set and b & seg4_set != seg4_set:
				seg[5] = b & seg2_set
				seg[2] = seg2_set ^ seg[5]
		
				seg[6] = b & seg4_set
				seg[4] = seg4_set ^ seg[6]
		elif len(p) == 6:
			b = pattern_to_bits(p)
			if b & seg1_set != seg1_set:
				seg[1] = b & seg1_set
				seg[3] = seg1_set ^ seg[1]

	digits = [
		0b1110111, #0
		0b0100100, #1
		0b1011101, #2
		0b1101101, #3
		0b0101110, #4
		0b1101011, #5
		0b1111011, #6
		0b0100101, #7
		0b1111111, #8
		0b1101111, #9
	]

	def decode(e):
		d = 0
		for c in e:
			d |= 1 << seg.index(1 << (ord(c) - ord('a')))
		return digits.index(d)

	solution = sum(decode(encoded[n]) * 10**(3 - n) for n in range(4))
	return solution

f = open("input")
problems = f.read().splitlines()
total = 0
for p in problems:
	total += solve(p)

print(total)