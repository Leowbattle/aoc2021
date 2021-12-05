import re
import itertools as it
from dataclasses import dataclass

@dataclass
class Line:
	x1: int
	y1: int
	x2: int
	y2: int

f = open("input")
lines = f.read().splitlines()

line_re = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
lines = [Line(*map(int, line_re.match(l).groups())) for l in lines]

width  = max(it.chain.from_iterable([l.x1, l.x2] for l in lines)) + 1
height = max(it.chain.from_iterable([l.y1, l.y2] for l in lines)) + 1

grid = [[0] * width for _ in range(height)]

def printGrid():
	print('\n'.join(''.join(map(str, row)) for row in grid).translate({ord('0'): ord('.')}))
	print()

for l in lines:
	if l.x1 == l.x2:
		# vertical line

		if l.y1 > l.y2:
			l.y1, l.y2 = l.y2, l.y1

		for y in range(l.y1, l.y2 + 1):
			grid[y][l.x1] += 1
	elif l.y1 == l.y2:
		# horizontal line

		if l.x1 > l.x2:
			l.x1, l.x2 = l.x2, l.x1

		for x in range(l.x1, l.x2 + 1):
			grid[l.y1][x] += 1
	else:
		print(l)

		if l.x1 > l.x2:
			l.x1, l.x2 = l.x2, l.x1
			l.y1, l.y2 = l.y2, l.y1

		dy = 1 if l.y2 > l.y1 else -1

		y = l.y1
		for x in range(l.x1, l.x2 + 1):
			grid[y][x] += 1
			y += dy

printGrid()
score = sum(num >= 2 for row in grid for num in row)
print(score)