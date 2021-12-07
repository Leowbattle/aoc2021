f = open("input")
crabs = list(map(int, f.read().split(',')))

# calculate the fuel cost for all crabs to go to position pos
def cost(pos):
	total = 0
	for c in crabs:
		dist = abs(pos - c)
		total += dist * (dist + 1) // 2
	return total

m = sum(crabs) / len(crabs)
print(min(cost(int(m + 0.5)), cost(int(m - 0.5))))
