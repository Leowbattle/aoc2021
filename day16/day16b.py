from functools import reduce
from operator import mul

digits = {
	'0': '0000',
	'1': '0001',
	'2': '0010',
	'3': '0011',
	'4': '0100',
	'5': '0101',
	'6': '0110',
	'7': '0111',
	'8': '1000',
	'9': '1001',
	'A': '1010',
	'B': '1011',
	'C': '1100',
	'D': '1101',
	'E': '1110',
	'F': '1111',
}

f = open("input")
b = "".join(digits[c] for c in f.read())

i = 0

def getbits(n):
	global b, i
	i += n
	bits = b[:n]
	b = b[n:]
	return int(bits, base=2)

def align(n):
	n -= 1
	i2 = (i + n) & ~n
	getbits(i2 - i)

def literal():
	num = 0
	while True:
		more_bits = getbits(1)
		num <<= 4
		num |= getbits(4)
		if not more_bits:
			break
	
	return num

def operator(type_id):
	global i

	args = []

	len_type = getbits(1)
	if len_type == 0:
		bit_len = getbits(15)
		i_start = i
		while i - i_start < bit_len:
			args.append(packet())
	else:
		num_packets = getbits(11)
		for i2 in range(num_packets):
			args.append(packet())

	if type_id == 0:
		return sum(args)
	elif type_id == 1:
		return reduce(mul, args)
	elif type_id == 2:
		return min(args)
	elif type_id == 3:
		return max(args)
	elif type_id == 5:
		return int(args[0] > args[1])
	elif type_id == 6:
		return int(args[0] < args[1])
	elif type_id == 7:
		return int(args[0] == args[1])

def packet():
	version = getbits(3)
	type_id = getbits(3)

	if type_id == 4:
		return literal()
	else:
		return operator(type_id)

print(packet())