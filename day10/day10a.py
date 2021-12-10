import re

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def score(l: str):
	while True:
		l2 = re.sub(r"\(\)|\[\]|\{\}|\<\>", "", l)

		if l == l2:
			break
		l = l2
	print(l2)
	l2 = re.sub(r"[([{<]", "", l2)
	if len(l2) == 0:
		return 0
	
	return scores[l2[0]]

f = open("input")
lines = f.read().splitlines()

total = sum(score(l) for l in lines)
print(total)