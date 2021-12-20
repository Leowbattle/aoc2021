f = open("test")
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
	global img

	img2 = set()
	for p in img:
		if getpixel(p):
			img2.add(p)
		
		x, y = p
		for j in range(y - 1, y + 2):
			for i in range(x - 1, x + 2):
				p2 = (i, j)
				if p2 not in img2 and getpixel(p2):
					img2.add(p2)

	img = img2