from collections import defaultdict

f = open("input")

caves = defaultdict(list)

for l in f.read().splitlines():
	a, b = l.split('-')
	caves[a].append(b)
	caves[b].append(a)

sizes = {a: "big" if a.isupper() else "small" for a in caves}

# find all paths from a to end
def find_paths(a: str, marked: set):
	paths = []

	if sizes[a] == "small":	
		marked.add(a)

	for b in caves[a]:
		if b == "end":
			paths.append([a, "end"])
			continue

		if b in marked:
			continue

		for p in find_paths(b, marked):
			paths.append([a, *p])

	if sizes[a] == "small":	
		marked.remove(a)

	return paths

paths = find_paths("start", set())
# paths.sort()
# for p in paths:
# 	print(",".join(p))

print(len(paths))