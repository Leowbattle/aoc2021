from dataclasses import dataclass
from typing import List

row_win = 0b1111100000000000000000000
col_win = 0b1000010000100001000010000

@dataclass
class Board:
	nums: List[int]
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

f = open("input").read()

nums, *boards = f.split("\n\n")
nums = nums.split(',')
boards = [Board(b.split(), 0) for b in boards]

def get_winner():
	for num in nums:
		for b in boards:
			try:
				i = b.nums.index(num)
				b.marked |= (1 << i)
				if b.is_winner():
					return b, int(num)
			except ValueError:
				pass

winner, num = get_winner()
score = num * winner.sum_unmarked()
print(f"score = {score}")