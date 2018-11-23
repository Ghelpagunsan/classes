
class manipulating:
	def __init__(self, n):
		self.n = n

	def splitting(self):
		return str(self.n.split(" "))

	def concatenate(self):
		x = "Holy"
		y = (str(x) + str(self.n))
		return y

	def length(self):
		m = len(self.n)
		return m

	def position(self,x):
		return str(x[5])

	def whitespace(self):
		return self.n.strip()

	def lowercasing(self):
		return str(self.n.lower())

	def uppercasing(self):
		return str(self.n.upper())


class looping:
	def __init__(self, n):
		self.n = n

	def forlooping(self):
		for i in self.n:
			print(i)

	def whilelooping(self):
		x= len(self.n) - 1
		while x >= 0:
			print(self.n[x])
			x-=1


class compare:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def ifstate(self):
		n = len(self.x)
		z = len(self.y)
		if z == n:
			return str("Match")
		else:
			return str("Unmatch")

	def elifstate(self):
		n = len(self.x)
		z = len(self.y)
		if z == n:
			return str("Match")
		elif n<self.x:
			return str("Add more")
		else:
			return str("Unmatch")

	def range(self, n):
		return str(n[3:6])


class string_array:
	def __init__(self, n):
		self.n = n

	def names(self):
		for x in self.n:
			print(x)

	def numbering(self):
		for a, b in enumerate(self.n):
			print(a, b)


class changing:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def replacing(self, n):
		x = (n.replace("n", "m"))
		return x

	def check(self ,n):
		if  "hi" in n:
			return str("Existing")
		else:
			return str("add!")

	def counting(self, n):
		x = (n.count(5))
		return x

	def inttostr(self, n):
		return str(n)

	def adding(self):
		c = self.a + self.b
		return str(len(c))

	def subtracting(self):
		x = len(self.a)
		y = len(self.b)
		c = x - y
		return str(c)






# print(splitting("2 5 3 5"))
# print(concatenate("Cross"))
# print(length("qwertyuiop"))
# print(position("trinity"))
# print(whitespace("Call maybe"))
# print(lowercasing("AMAZING"))
# print(uppercasing("good job"))
# forlooping("Morning")
# whilelooping("Evening")
# print(ifstate("seven"))
# print(elifstate("torment"))
# print(range("moment"))
# names()
# numbering()
# print(replacing("nick"))
# print(check())
# print(counting())
# print(inttostr(234))
# print(adding())
# print(subtracting())