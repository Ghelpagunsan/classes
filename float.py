import math

class Processes:
	def __init__(self, y, z):
		self.y = y
		self.z = z

	def division(self):
		return float(self.y/self.z)

	def addition(self):
		c = self.y + self.z
		d = ("%.2f" % c)
		return d

	def multiplication(self):
		return (self.y*self.z)

	def subtraction(self):
		return (self.y-self.z)


class conditional_statements:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def ifstate(self):
		if self.x<=self.y and self.z>self.x:
			return self.y
		else:
			return self.x 

	def elseif(self):
		if self.x==self.y and self.y==self.z:
			return self.x
		elif self.x==self.y and self.z<self.y:
			return self.y
		else:
			return self.z

class random:
	def __init__(self, s, e):
		self.s = s
		self.e = e

	def forstate():
		n = [float(x)/10 for x in range(10)]
		return n

	def whilestate(self):
		x = self.s
		while x<=self.e:
			return x
			x+=1

	def floordiv(self):
		x = self.s
		y = self.e
		z = x // y
		return z

class area:
	def __init__(self,x, y, z):
		self.x = x
		self.y = y
		self.z = z


	def rectangle(self, x, y):
		area = x*y
		float(area)
		z = ("the area of rectangle is %.2f" %area)
		return str(z)

	def circle(self, y):
		cir = (math.pi * (self.y*self.y))
		float(cir)
		c  = ("circle's area is %.2f cm" %cir)
		return str(c)

	def pyramid(self, n):
	    x = 1
	    while (x <= n):
	        print("1.01" * x)
	        x = x + 1
	    return

	def triangle(self, a, b):
		x = a * a
		y = b * b
		z = math.sqrt(x+y)
		i = ("%.2f is the hypotenuse" %z)
		return str(i) 

	def cylinder(self, r, h):
		x = r
		y = h
		a = 2 * (math.pi * (x * y))
		b = 2 * (math.pi *(x * x))
		area = a + b
		z = ("cylinder's area is %.2f" % area)
		return str(z)

	def tangent(self, x, y):
		tan = (x/y)
		return tan

	def parallel(self, b, h):
		x = (b*h)
		return x

	def trap(self):
		area = ((self.x+self.y)/2) * self.z
		return area

	def square(self, x):
		area = x * x * x * x
		y = ("area of the square %.2f" %area)
		return str(y)

	def volume(self, r, h):
		a = r
		b = h
		vol = math.pi*(a*a)*b
		return vol

	def cone(self, r, h):
		x = r
		y = h
		a = math.pi * x
		b = x + (math.sqrt((y*y) + (x*x)))
		area = a * b
		return str("cone area is %.2f" % area)




# print(division(2.5, 16.3))
# print(addition(4.5, 6.3))
# print(multiplication(3.3, 4.5))
# print(subtration(13.45, 6.3))
# print(ifstate(12.01, 12.001))
# print(elseif(2.01, 2.101, 2.001))
# print(forstate())
# print(whilestate(1.1, 10.1))
# print(floordiv(200.1))
# print(rectangle(4, 5.3))
# print(circle(17.4))
# pyramid(8)
# print(triangle(4.2, 6.1))
# print(cylinder(5,5.7))
# print(tangent(26.0, 15.0))
# print(parallel(5.4, 8.1))
# print(trap(3.4, 2.8, 10.2))
# print(square(3.4))
# print(volume(3, 5.5))
# print(cone(4.3, 7))
