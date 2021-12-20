from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int
	z: int
	
	def __repr__(self):
		return str(f"{self.x},{self.y},{self.z}")

def rotate


points = [
	Point(-1,-1,1),
	Point(-2,-2,2),
	Point(-3,-3,3),
	Point(-2,-3,1),
	Point(5,6,-4),
	Point(8,0,7),
]
