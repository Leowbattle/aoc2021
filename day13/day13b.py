import re

f = open("input")
dots, folds = f.read().split("\n\n")

dots = [d.split(",") for d in dots.splitlines()]
dots = [(int(d[0]), int(d[1])) for d in dots]

folds = [re.match(r"fold along ([xy])=(\d+)", fold).groups() for fold in folds.splitlines()]
folds = [(fold[0], int(fold[1])) for fold in folds]

width =  max(d[0] for d in dots) + 1
height = max(d[1] for d in dots) + 1

paper = [['.'] * width for _ in range(height)]
def print_paper():
	print("\n".join("".join(row) for row in paper))

for x, y in dots:
	paper[y][x] = '#'

def merge_rows(a, b):
	return ['#' if a[i] == '#' or b[i] == '#' else '.' for i in range(len(a))]

def do_x_fold():
	global width, paper

	width //= 2

	left =  [[paper[i][j] for i in range(height)] for j in range(width)]
	right = [[paper[i][j] for i in range(height)] for j in range(width + 1, len(paper[0]))]
	right.reverse()

	paper = [merge_rows(a, b) for a, b in zip(left, right)]

	paper = [[paper[i][j] for i in range(width)] for j in range(height)]

def do_y_fold():
	global height, paper

	height //= 2

	top = paper[:height]
	bottom = paper[height + 1:]
	bottom.reverse()

	paper = [merge_rows(a, b) for a, b in zip(top, bottom)]

def do_fold(fold):
	if fold[0] == 'x':
		do_x_fold()
	elif fold[0] == 'y':
		do_y_fold()

for fold in folds:
	do_fold(fold)

print_paper()

score = sum(row.count('#') for row in paper)
print(score)