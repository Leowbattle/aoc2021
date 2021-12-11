import itertools as it

f = open("input")

octopuses = [[int(c) for c in l] for l in f.read().splitlines()]
width = len(octopuses[0])
height = len(octopuses)

def get(p):
	return octopuses[p[1]][p[0]]

def adjacent(p):
	x, y = p
	a = []
	if x != 0:
		a.append((x - 1, y))
		if y != 0:
			a.append((x - 1, y - 1))
		if y != height - 1:
			a.append((x - 1, y + 1))
	if x != width - 1:
		a.append((x + 1, y))
		if y != 0:
			a.append((x + 1, y - 1))
		if y != height - 1:
			a.append((x + 1, y + 1))
	if y != 0:
		a.append((x, y - 1))
	if y != height - 1:
		a.append((x, y + 1))
	return a	

def board_str():
	return "\n".join("".join(str(o) for o in l) for l in octopuses)

def step():
	flashers = set()
	flashed = set()

	def step_pos(p):
		x, y = p
		energy = octopuses[y][x] + 1
		if energy > 9:
			if p not in flashed:
				flashers.add(p)
		octopuses[y][x] = energy

	for p in it.product(range(width), range(height)):
		step_pos(p)

	while len(flashers) > 0:
		p = flashers.pop()
		flashed.add(p)
		for a in adjacent(p):
			step_pos(a)
		
	for x, y in flashed:
		octopuses[y][x] = 0

	return len(flashed)

score = next(i + 1 for i in it.count() if (s := step()) == 100)
print(score)