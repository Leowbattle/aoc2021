"""
For part 2 you need to find the last board to win, so every time a board wins I add it to the set of all boards that have won. Once the set contains every board, return the last board that was added.

To make that work, a few minor changes had to be made to the rest of the program. In Python, an object can only be added to a set or dict if it is hashable, which dataclasses are not by default. I also couldn't use dataclass's built-in hash function because I only want the hash based off nums, so I wrote my own __hash__. nums had to be changed from List to Tuple because Lists can not be hashed, a tuple is an immutable list that can be hashed.
"""

from dataclasses import dataclass
from typing import Tuple

row_win = 0b1111100000000000000000000
col_win = 0b1000010000100001000010000

@dataclass
class Board:
	nums: Tuple[int]
	marked: int

	def is_winner(self):
		for i in range(5):
			r = row_win >> (i * 5)
			c = col_win >> i
			if (self.marked & r == r) or (self.marked & c == c):
				return True
		return False

	def sum_unmarked(self):
		return sum(int(self.nums[i]) for i in range(len(self.nums)) if (self.marked & (1 << i)) == 0)

	def __hash__(self):
		return hash(self.nums)

f = open("input").read()

nums, *boards = f.split("\n\n")
nums = nums.split(',')
boards = [Board(tuple(b.split()), 0) for b in boards]

def get_winner():
	winners = set()

	for num in nums:
		for b in boards:
			try:
				i = b.nums.index(num)
				b.marked |= (1 << i)
				if b.is_winner():
					winners.add(b)
					if len(winners) == len(boards):
						return b, int(num)
			except ValueError:
				pass

winner, num = get_winner()
score = num * winner.sum_unmarked()
print(f"score = {score}")