from collections import Counter

f = open("input")
lines = f.read().splitlines()
width = len(lines[0])

def get_rating(which):
	pref = '1' if which == "oxygen" else '0'

	nums = lines.copy()
	for i in range(width):	
		c = Counter(l[i] for l in nums)
		if which == "co2":
			c['0'], c['1'] = c['1'], c['0']

		if c['0'] == c['1']:
			b = pref
		else:
			b = c.most_common(1)[0][0]
		
		nums = [n for n in nums if n[i] == b]

		if len(nums) == 1:
			return nums[0]

oxygen = int(get_rating("oxygen"), base=2)
co2 = int(get_rating("co2"), base=2)

print(f"oxygen = {oxygen} co2 = {co2}")
print(f"life = {oxygen * co2}")