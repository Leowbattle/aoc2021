from functools import reduce

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

def completion_string(l):
	stack = []
	for c in l:
		if c in pairs:
			stack.append(pairs[c])
		elif c in pairs.values():
			if c == stack[-1]:
				stack.pop()
			else:
				return None
	
	stack.reverse()
	return stack

def score(s):
	return reduce(lambda a, c: 5 * a + points[c], s, 0)

f = open("input")
lines = f.read().splitlines()

scores = []
for l in lines:
	s = completion_string(l)
	if s:
		scores.append(score(s))

scores.sort()
print(scores[len(scores) // 2])