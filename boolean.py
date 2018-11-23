	
class compute:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def check(self, n):
		x = n
		return(bool(x%2==0))
		# x = 4
		# if (check(x)):
		# 		print("Even Number-True")
		# else:
		# 	print("Odd Number-False")

	def notequal(self):
		return(bool(self.x==self.y))

	def array(self, x):
		return(bool(x))

	def add(self):
		z = self.x + self.y
		if z == 11:
			return str("8+3 is 11 " + str(bool(z)))
		else:
			return str("False")

	def sub(self):
		z = self.x - self.y
		if z < 0:
			return("Negative!" + str(bool(z)))
		else:
			return("Positive!" + str(bool(z)))

	def prod(self):
		z = self.x * self.y
		if bool(z%10==0):
			return True
		elif bool(z%10!=0):
			return False

	def quo(self):
		c = self.x/self.y
		d = 5
		if c == 5:
			return bool(c==d)
		else:
			return bool(c==d)

	def ifst(self):
		if self.x>self.y:
			return bool(self.x>self.y)
		else:
			return bool(self.x>self.y)

	def elifst(self):
		#x =13
		#y=4
		if self.x < self.y:
			return bool(self.x<self.y)
		elif self.x == self.y:
			return bool(self.x==self.y)
		else:
			return bool(self.x>self.y)

	
class check:
	def __init__(self, n):
		self.n = n

	def none(self):
		self.n = None
		return bool(self.n)

	def string(self, x):
		y = x, 'is', bool(x)
		return str(y)

	def integer(self):
		return bool(self.n)

	def whileloop(self):
		while True:
			if self.n == 4:
				return True
				break
			else:
				return False
				break

	
class evaluate:
	def __init__(self, x):
		self.x = x

	def expression(self, a, b):
		x = (4, not a and b )
		return str(x)

	def mapping(self, map):
		return bool(map)

	def forloop(self, arr):
		a = 0
		for i in arr:
			return bool(i)
			a+=1

	def float(self, n):
		return bool(n)

	def boolean(self, variable):
		if variable == True:
		    return str("The function is True!")
		else:
		    return str("The function is False.")


	def andstate(self):
		boolean = True
		y = ((self.x>=5) and (boolean==True))
		return y

	def orstate(self):
		boolean = False
		b = ((self.x<6) or (boolean==False))
		return b






#-----------------------------------------------#


# print(check(12))
# print(notequal())
# print(array())
# print(add())
# print(sub(5, 2))
# print(prod(5, 4))
# print(quo(10, 4))
# print(ifst(5, 3))
# print(elifst())
# print(none())
# print(string())
# print(integer(0))
# print(whileloop(4))
# print(expression())
# print(mapping())
# print(forloop([1]))
# print(float(0.0))
# print(boolean())
# print(andstate(3))
# print(orstate(4))