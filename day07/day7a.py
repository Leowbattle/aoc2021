f = open("input")
crabs = sorted(map(int, f.read().split(',')))

# calculate the fuel cost for all crabs to go to position pos
def cost(pos):
	return sum(abs(pos - c) for c in crabs)

print(cost(crabs[len(crabs) // 2]))
