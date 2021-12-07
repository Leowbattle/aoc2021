f = open("input")
crabs = sorted(map(int, f.read().split(',')))

from math import comb
# calculate the fuel cost for all crabs to go to position pos
def cost(pos):
	return sum(comb(abs(pos - c) + 1, 2) for c in crabs)

lastCost = cost(0)
for c in range(crabs[-1]):
	newCost = cost(c)
	if newCost > lastCost:
		break
	lastCost = newCost

print(lastCost)