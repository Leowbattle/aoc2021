f = open("input")
fish = list(map(int, f.read().split(',')))

#print(f"Initial state: {','.join(map(str, fish))}")

for i in range(1, 81):
	for j in range(len(fish)):
		fish[j] -= 1
		if fish[j] < 0:
			fish[j] = 6
			fish.append(8)

	#print(f"After {i:>2} {'day: ' if i == 1 else 'days:'} {','.join(map(str, fish))}")

print(len(fish))