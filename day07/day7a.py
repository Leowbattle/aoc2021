f = open("input")
crabs = sorted(map(int, f.read().split(',')))

# calculate the fuel cost for all crabs to go to position pos
def cost(pos):
	return sum(abs(pos - c) for c in crabs)

lastCost = cost(0)
for c in crabs:
	newCost = cost(c)
	if newCost > lastCost:
		pos = c
		break
	lastCost = newCost

print(lastCost)