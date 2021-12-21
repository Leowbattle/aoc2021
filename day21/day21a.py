from dataclasses import dataclass

@dataclass
class Player:
	pos: int
	score: int

p1 = Player(7, 0)
p2 = Player(2, 0)

def wrap(x, n):
	return (x - 1) % n + 1

die = 1
numRolls = 0

def turn(p: Player):
	global numRolls, die

	for i in range(3):
		p.pos = wrap(p.pos + die, 10)

		numRolls += 1
		die += 1

	p.score += p.pos
	return p.score >= 1000

while True:
	if turn(p1):
		loser = p2
		break
	if turn(p2):
		loser = p1
		break

print(numRolls * loser.score)