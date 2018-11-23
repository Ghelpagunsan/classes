
class Operation:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def add(self):
		c=self.x+self.y
		return c


	def subtract(self, n):
		return 100 - n

	def multiply(self):
		return self.x*self.y

	def divide(self, n):
		return 100 / n

	def cont(self, age):
		c = "I am " + str(age) + " years old"
		return c

	def greater(self):
		if self.x<self.y:
			return self.x
		else:
			return self.y

	def lesser(self, n):
		a = 15
		b = str("I lose")
		c = str("i Win")
		if a<n:
			return b
		else:
			return c

	
class iteration:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def recursion(self, n):
		if n<=20:
			return n
		else:
			return n * recursion(n+1)

	def equal(self):
		if self.a==self.b:
			return str("Match")
		else:
			return str("Nah")

	def forloop(self, sum):
		for i in sum:
			return sum

	def whileloop(self, i):
		while i<6:
			return i
			i+=1

class comparison:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def ifstate(self):
		if self.a<=self.b:
			return str("Yey")
		else:
			return str("Nay")

	def elifstate(self):
		if self.a<self.b:
			return self.a+self.b
		elif self.a>self.b:
			return self.a-self.b
		else:
			return self.a*self.b

	def swap(self):
		c = str("Before swap a = %d and b = %d" %(self.a, self.b))
		self.a, self.b = self.b, self.a
		d = str("After swaping a = %d and b = %d" %(self.a, self.b))
		return str(c + "\n" + d)


class number:
	def __init__(self, n):
		self.n = n

	def insert(self, sum):
		#sum = [1,2,3]
		sum.insert(3, 4)
		a = sum[3]
		return a

	def popnum(self, x):
		x.pop()
		return x

	def triangle(self):
	    x = 1
	    while (x <= self.n):
	        print("1" * x)
	        x = x + 1
	    return

	def count(self, xam):
		#xam = [1,1,1,2,2]
		f=0
		l=0
		for i in xam:
			if i==1:
				f+=1
			elif i==2:
				l+=1
		a = str("number of one found %d" %f)
		b = str("number of two found %d" %l)
		return str(a + "\n" + b)

	def plainprint(self):
		return self.n
		

	def convert(self):
		i = int(self.n)
		return i 



# print(substract(50))
# print(add())
# print(multiply())
# print(int(divide(2)))
# print(cont(20))
# print(greater(5, 6))
# print(lesser(20))
# print(int(recursion(20)))
# print(equal(21))
# print(forloop())
# print(whileloop())
# print(ifstate())
# print(elifstate(4, 5))
# print(swap(3,5))
# print(insert([1,2,3]))
# print(popnum())
# triangle(6)
# print(count([1,1,1,2,2]))
# print(plainprint())
# print(convert("123456"))