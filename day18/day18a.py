from dataclasses import dataclass
from ast import literal_eval

def isint(x):
	return type(x) == int

@dataclass
class Num:
	val: int = None
	left: "Num" = None
	right: "Num" = None
	parent: "Num" = None

	def from_arr(a):
		if isint(a):
			return Num(a)
		n = Num()
		l = Num.from_arr(a[0])
		l.parent = n
		r = Num.from_arr(a[1])
		r.parent = n
		n.left = l
		n.right = r
		return n

	def to_arr(self):
		if self.val != None:
			return self.val
		return [self.left.to_arr(), self.right.to_arr()]

	def inorder_prev(self):
		p1 = self
		p2 = self.parent
		while p2.left is p1:
			p1 = p2
			p2 = p2.parent
			if p2 == None:
				return None
		
		prev = p2.left
		while prev.val == None:
			prev = prev.right
		return prev

	def inorder_next(self):
		p1 = self
		p2 = self.parent
		while p2.right is p1:
			p1 = p2
			p2 = p2.parent
			if p2 == None:
				return None
		
		prev = p2.right
		while prev.val == None:
			prev = prev.left
		return prev

	def reduce(self):
		# print(self.to_arr())
		while self.reduce0(0):
			# print(self.to_arr())
			pass
		# print(self.to_arr())

	def reduce0(self, depth):
		if self.val != None:
			if self.val < 10:
				return False

			self.left = Num(val=self.val // 2, parent=self)
			self.right = Num(val=(self.val + 1) // 2, parent=self)
			self.val = None

			return True

		if depth == 4:
			l = self.left.val
			r = self.right.val

			self.val = 0
			self.left = None
			self.right = None

			if x := self.inorder_prev():
				x.val += l

			if x := self.inorder_next():
				x.val += r

			return True

		if self.left.reduce0(depth + 1):
			return True
		if self.right.reduce0(depth + 1):
			return True

# n = [[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
# num = Num.from_arr(n)
# num.reduce()
# print(num.to_arr())

f = open("test")
nums = [Num.from_arr(literal_eval(l)) for l in f.read().splitlines()]

result = nums[0]
print(result.to_arr())
for n in nums[1:]:
	res = Num(left=result, right=n)
	result.parent = res
	n.parent = res
	res.reduce()
	result = res
	print(result.to_arr())
