from functools import reduce
import operator

f = open("input")
nums = [[int(c) for c in l] for l in f.read().splitlines()]
width = len(nums[0])
height = len(nums)

def get(p):
	return nums[p[1]][p[0]]

unfilled = {(x, y) for x in range(width) for y in range(height) if get((x, y)) < 9}

def fill(p):
	size = 1

	adjacent = [
		(p[0] - 1, p[1]),
		(p[0] + 1, p[1]),
		(p[0], p[1] - 1),
		(p[0], p[1] + 1),
	]
	for a in adjacent:
		if a in unfilled:
			unfilled.remove(a)
			size += fill(a)

	return size

sizes = []

while len(unfilled) > 0:
	p = unfilled.pop()
	sizes.append(fill(p))

largest = sorted(sizes)[-3:]
score = reduce(operator.mul, largest)
print(score)