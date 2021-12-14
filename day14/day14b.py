from collections import Counter

f = open("input")
polymer, rules = f.read().split("\n\n")
rules = dict(rule.split(" -> ") for rule in rules.splitlines())

element_counts = Counter(polymer)
polymer = Counter(''.join(pair) for pair in zip(polymer, polymer[1:]))

def step():
	p = Counter()

	for pair, count in polymer.items():
		if pair in rules:
			replace = rules[pair]
			p[pair[0] + replace] += count
			p[replace + pair[1]] += count
			
			element_counts[replace] += count
		else:
			p[pair] += count

	return p

for i in range(40):
	polymer = step()

score = element_counts.most_common()[0][1] - element_counts.most_common()[-1][1]
print(score)