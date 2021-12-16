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
	
	# print(num)

def operator():
	global i

	len_type = getbits(1)
	if len_type == 0:
		bit_len = getbits(15)
		i_start = i
		while i - i_start < bit_len:
			packet()
	else:
		num_packets = getbits(11)
		for i2 in range(num_packets):
			packet()

version_sum = 0

def packet():
	global version_sum

	version = getbits(3)
	type_id = getbits(3)

	version_sum += version

	if type_id == 4:
		literal()
	else:
		operator()

packet()
print(version_sum)