from collections import Counter

f = open("input")
fish = Counter(map(int, f.read().split(',')))

for i in range(1, 257):
	fish2 = Counter()
	for time, count in fish.items():
		time -= 1
		if time < 0:
			time = 6
			fish2[8] += count
		fish2[time] += count
	fish = fish2

print(fish)
print(fish.total())