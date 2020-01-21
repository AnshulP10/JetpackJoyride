import sys 

def pos(x, y):
    return '\x1b[%d;%dH' % (x,y)

class Board:
	def __init__(self, X, Y):
		self.width = X
		self.height = Y
		self.grid = [[" " for x in range(self.width)] for y in range(self.height)]
		for x in range(self.width):
			self.grid[self.height-1][x] = 'X'

	def make(self):
		for y in range(self.height):
			for x in range(5, self.width-5):
				print(f"{pos(y,x)}{self.grid[y][x]}") 
				pass	
