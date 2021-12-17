f = open("input")
a, b = map(int, f.read().split("y=")[1].split(".."))

uy = 0
n = 0

max_y = 0

while True:
	sy = n * (2 * uy + 1 - n) // 2
	n += 1

	if a <= sy <= b:
		max_y = (uy * (uy + 1)) // 2
		print(max_y)
	elif sy < a:
		uy += 1

# I don't know what the exit condition for this algorithm looks like, so I just run it until it looks like it won't make a better solution, then Ctrl-C it.