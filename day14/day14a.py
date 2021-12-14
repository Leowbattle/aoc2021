from collections import Counter

f = open("input")
polymer, rules = f.read().split("\n\n")
rules = dict(rule.split(" -> ") for rule in rules.splitlines())

def step():
	p = []

	for i in range(len(polymer) - 1):
		p.append(polymer[i])
		pair = polymer[i:i+2]
		if pair in rules:
			p.append(rules[pair])

	p.append(polymer[-1])
	
	return "".join(p)

for i in range(10):
	polymer = step()

c = Counter(polymer)
score = c.most_common()[0][1] - c.most_common()[-1][1]
print(score)