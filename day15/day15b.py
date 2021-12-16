import heapq

f = open("input")
nums = [[int(x) for x in l] for l in f.read().splitlines()]

num_repeats = 5

data_width = len(nums[0])
data_height = len(nums)

width = data_width * num_repeats
height = data_height * num_repeats

def get(p):
	qx, rx = divmod(p[0], data_width)
	qy, ry = divmod(p[1], data_height)

	risk = nums[ry][rx]
	for _ in range(qx + qy):
		risk += 1
		if risk > 9:
			risk = 1
	return risk

def adjacent(p):
	x, y = p
	a = []
	if x != 0:
		a.append((x - 1, y))
	if x != width - 1:
		a.append((x + 1, y))
	if y != 0:
		a.append((x, y - 1))
	if y != height - 1:
		a.append((x, y + 1))
	return a

def board_str():
	return "\n".join("".join(str(get((x, y))) for x in range(width)) for y in range(height))

def dijkstra(start, end):
	frontier = [(get(a), a) for a in adjacent(start)]
	heapq.heapify(frontier)

	previous = {a[1]: start for a in frontier}
	previous[start] = None

	while len(frontier) > 0:
		cost, pos = heapq.heappop(frontier)
		for a in adjacent(pos):
			if a not in previous:
				heapq.heappush(frontier, (cost + get(a), a))
				previous[a] = pos

	path = [end]
	while p := previous[path[-1]]:
		path.append(p)
	path.reverse()
	return path

path = dijkstra((0, 0), (width - 1, height - 1))
risk = sum(get(pos) for pos in path) - get((0, 0))
print(risk)