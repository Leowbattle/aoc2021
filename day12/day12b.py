from collections import defaultdict

f = open("input")

caves = defaultdict(list)

for l in f.read().splitlines():
	a, b = l.split('-')
	caves[a].append(b)
	caves[b].append(a)

sizes = {a: "big" if a.isupper() else "small" for a in caves}

# find all paths from a to end
def find_paths(a: str, marked: defaultdict[str, int]):
	paths = []

	if sizes[a] == "small":	
		marked[a] += 1

	for b in caves[a]:
		if b == "start":
			continue

		if b == "end":
			paths.append([a, "end"])
			continue

		if 2 in marked.values() and marked[b] > 0:
			continue

		for p in find_paths(b, marked):
			paths.append([a, *p])

	if sizes[a] == "small":	
		marked[a] -= 1

	return paths

paths = find_paths("start", defaultdict(int))
# paths.sort()
# for p in paths:
# 	print(",".join(p))

print(len(paths))