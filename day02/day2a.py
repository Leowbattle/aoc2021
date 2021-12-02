f = open("input")
lines = f.read().splitlines()

cmds = map(lambda l: l.split(), lines)

horizontal = 0
depth = 0

for cmd in cmds:
	amount = int(cmd[1])
	if cmd[0] == "forward":
		horizontal += amount
	elif cmd[0] == "down":
		depth += amount
	elif cmd[0] == "up":
		depth -= amount

print(horizontal * depth)