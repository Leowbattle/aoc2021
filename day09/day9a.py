f = open("input")
nums = [[int(c) for c in l] for l in f.read().splitlines()]
width = len(nums[0])
height = len(nums)

padding = 10
border = [padding] * (width + 2)
nums = [border, *([padding, *l, padding] for l in nums), border]

def get(x, y):
	return nums[y + 1][x + 1]

def is_low(x, y):
	h = get(x, y)
	return (h < get(x - 1, y) and
			h < get(x + 1, y) and 
			h < get(x, y - 1) and 
			h < get(x, y + 1))

risk = sum(get(x, y) + 1 for x in range(width) for y in range(height) if is_low(x, y))

print(risk)