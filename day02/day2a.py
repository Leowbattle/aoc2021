import re

f = open("input")
lines = f.read().splitlines()

cmd_re = re.compile(r"(forward|down|up) (\d+)")
cmds = map(lambda l: cmd_re.match(l).groups(), lines)

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