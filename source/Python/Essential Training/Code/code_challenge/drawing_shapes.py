# Python code​​​​​​‌‌‌​​​‌​​‌‌‌​‌‌‌​‌​‌​‌​​​ below
class Shape:
	width = 5
	height = 5
	printChar = '*'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	
	height = 5
	width = 2 * height
	
	def printRow(self,i):
		trianglewidth = i*2+1
		padding = int((self.width - trianglewidth)/2)
		print(' ' * padding + self.printChar * trianglewidth)
		
'''
	def printRow(self, i):
		print(self.printChar * (i + 1))
    '''
s = Square()
t = Triangle()

s.print()
t.print()