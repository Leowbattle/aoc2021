"""
In day4a I got my first incorrect answer by trying to be too clever.

In my solution bingo boards are stored as a list of numbers and a 25-bit integer that stores which have been marked (1 bit for each number in a 5x5 board). This means it is possible to detect winners efficiently using bitwise operators. For ease of demonstration I will use a 2x2 board:

31 23
27 89

nums: [31, 23, 27, 89]
marked: 0b1000

In order to detect a winner, you check to see if any rows or columns are completely filled in using a bitmask.
Items in the same row are stored adjacently so the bitmask is 0b1100 for the first row and 0b0011 for the second row. The bitmask for the nth row is (0b11 >> (n * 2)).
Items in the same column are stored in every nth item in an n-by-n board, in this case every 2nd item, so the bitmask is 0b1010 for the first column and 0b0101 for the second column. The bitmask of the nth column is (0b1010 >> n).

So does the example board win?
0b1000 & 0b1100 != 0b1100, it doesn't win by the first row.
0b1000 & 0b0011 != 0b0011, it doesn't win by the second row.
0b1000 & 0b1010 != 0b1010, it doesn't win by the first column.
0b1000 & 0b0101 != 0b0101, it doesn't win by the second column.

So the board doesn't win. If marked is changed to 0b1100 then the board wins by the first row.

The reason that I got an incorrect answer is because in `Board.is_winner` I wrote `c = col_win << i`, where it should have been `>>`. I then assumed that if the code produces the correct answer on the example data it will also product the correct answer for the puzzle input. However the example data won using a row, so I didn't realise that the column win testing code was incorrect, and coincidentally my puzzle input won using a column, which my program could not detect.

Interestingly, the incorrect code may have worked anyway because the puzzle input is randomised for each person and I assume that it is a 50-50 chance wether a given puzzle input wins using a row or column. However I would rather get the incorrect answer and fix the program than get a correct answer and unknowingly leave the program broken forever.

Note: Even though it is not required for the challenge, the bitmask method is also capable of detecting diagonal wins, using the bitmasks 0b10000_01000_00100_00010_00001 and 0b00001_00010_00100_01000_10000.
"""

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