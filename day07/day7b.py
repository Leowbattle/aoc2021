f = open("input")
crabs = sorted(map(int, f.read().split(',')))

# calculate the fuel cost for all crabs to go to position pos
def cost(pos):
	total = 0
	for c in crabs:
		dist = abs(pos - c)
		total += dist * (dist + 1) / 2
	return total

def sign(x):
	return 1 if x >= 0 else -1

def g(pos):
	return sum(pos - c + 0.5*sign(pos - c) for c in crabs)

p = -g(0) / len(crabs)
print(f"approximate O(n) solution: {cost(p)}")
