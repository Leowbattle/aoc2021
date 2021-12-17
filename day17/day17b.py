ax, bx = 96, 125
ay, by = -144, -98

def check(vx, vy):
	x, y = 0, 0
	while True:
		x += vx
		y += vy

		if vx > 0:
			vx -= 1
		elif vx < 0:
			vx += 1
		vy -= 1

		if ax <= x <= bx and ay <= y <= by:
			return True
		if x > bx or y < ay:
			return False

count = 0
for vx in range(1001):
	for vy in range(-1000, 1001):
		if check(vx, vy):
			count += 1
			# print(f"{vx},{vy}")
print(count)