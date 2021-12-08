"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""

digit_segments = [
	{0, 1, 2, 4, 5, 6},    #0
	{2, 5},                #1
	{0, 2, 3, 4, 6},       #2
	{0, 2, 3, 5, 6},       #3
	{1, 2, 3, 5},          #4
	{0, 1, 3, 5, 6},       #5
	{0, 1, 3, 4, 5, 6},    #6
	{0, 2, 5},             #7
	{0, 1, 2, 3, 4, 5, 6}, #8
	{0, 1, 2, 3, 5, 6},    #9
]

problem = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
patterns, encoded = problem.split(" | ")
patterns = [set(p) for p in patterns.split()]
encoded = [set(e) for e in encoded.split()]

def find_len(l):
	p = next(p for p in patterns if len(p) == l)
	patterns.remove(p)
	return p

#knowledge stores the set of all segments each segment is wired to.
#If the set for a segment contains 1 item, we know exactly what it is wired to.
knowledge = [set() for _ in range(7)]

def all_knowledge():
	return all(len(k) == 1 for k in knowledge)

pat_1 = find_len(2)
knowledge[2] |= pat_1
knowledge[5] |= pat_1

pat_7 = find_len(3)
knowledge[0] |= pat_7 - pat_1

pat_4 = find_len(4)
k = pat_4 - pat_1
knowledge[1] |= k
knowledge[3] |= k

pat_8 = find_len(7)
k = pat_8 - pat_1 - pat_7 - pat_4
knowledge[4] |= k
knowledge[6] |= k

print(knowledge)

def try_0(p: set[str]):
	if not (p.issuperset(knowledge[2]) and p.issuperset(knowledge[4])):
		return False

	new_knowledge = p - knowledge[2] - knowledge[4] - knowledge[0]
	knowledge[1] = new_knowledge
	knowledge[3] -= knowledge[1]

	return True

def try_6(p: set[str]):
	if not (p.issuperset(knowledge[1]) and p.issuperset(knowledge[4])):
		return False

	new_knowledge = p - knowledge[4] - knowledge[1] - knowledge[3] - knowledge[0]
	knowledge[5] = new_knowledge
	knowledge[2] -= new_knowledge

	return True

def try_9(p: set[str]):
	if not (p.issuperset(knowledge[2]) and p.issuperset(knowledge[1])):
		return False

	new_knowledge = p - knowledge[0] - knowledge[1] - knowledge[2] - knowledge[3] - knowledge[5]
	knowledge[6] = new_knowledge
	knowledge[4] -= new_knowledge

	return True

def try_2(p: set[str]):
	if not (p.issuperset(knowledge[4])):
		return False

	print("PANIC MODE")

	return True

while not all_knowledge():
	p = patterns.pop()
	print(len(p))
	if len(p) == 6:
		try_0(p) or try_6(p) or try_9(p)
	elif len(p) == 5:
		try_2(p)

print(knowledge)
knowledge = {knowledge[i].pop(): i for i in range(len(knowledge))}

def decode(e: set[str]):
	return digit_segments.index({knowledge[x] for x in e})
decoded = int("".join(str(decode(e)) for e in encoded))
print(decoded)