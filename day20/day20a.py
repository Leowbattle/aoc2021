f = open("input")
algo, img = f.read().split("\n\n")

img = [list(l) for l in img.splitlines()]
img = {(x, y) for y in range(len(img)) for x in range(len(img[0])) if img[y][x] == '#'}

def get(p):
	if p in img:
		return 1
	return 0

def img_str():
	minx = min(img, key=lambda p: p[0])[0]
	maxx = max(img, key=lambda p: p[0])[0]

	miny = min(img, key=lambda p: p[1])[1]
	maxy = max(img, key=lambda p: p[1])[1]

	return "\n".join("".join('#' if get((x, y)) == 1 else '.' for x in range(minx, maxx + 1)) for y in range(miny, maxy + 1))

def getpixel(p):
	x, y = p

	bits = 0
	for j in range(y - 1, y + 2):
		for i in range(x - 1, x + 2):
			bits <<= 1
			bits |= get((i, j))

	return algo[bits] == '#'

def enhance():
	global img, mode

	minx = min(img, key=lambda p: p[0])[0]
	maxx = max(img, key=lambda p: p[0])[0]

	miny = min(img, key=lambda p: p[1])[1]
	maxy = max(img, key=lambda p: p[1])[1]

	img2 = set()

	for x in range(minx - 10, maxx + 10):
		for y in range(miny - 10, maxy + 10):
			p = getpixel((x, y))
			if p:
				img2.add((x, y))

	img = img2

enhance()
enhance()

print(img_str())