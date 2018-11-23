	
class manipulate:
	def __init__(self, cars):
		self.cars = cars

	def add(self):
		self.cars.append("Ford")
		self.cars.sort()
		return self.cars

	def remove(self):
		print("Before removing" + str(self.cars))
		self.cars.remove("Honda")
		return str("After removing" + str(self.cars))

	def update(self, car):
		car.update(["Pajero", "Mitzubishi"])
		sorted(car)
		return car


class show:
	def __init__(self, num):
		self.num = num

	def getvalue(self):
		return str(self.num.index(4))

	def popval(self):
		self.num.pop()
		return self.num

	def reversing(self):
		self.num.reverse()
		return self.num


	def counting(self):
		i = 0
		for j in self.num:
			i+=1
		return i


class change:
	def __init__(self,year):
		self.year = year

	def deletingval(self):
		del self.year[3]
		return self.year

	def looping(self):
		for x in self.year:
			print(x)

	def check(self):
		if 2001 in self.year:
			return str("Found!")	


class compare:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def length(self, n):
		return str("The length of the list is " + str(len(n)))

	def multipleset(self, n):
		return str(n)
		y = n[0]
		return str(y)
		x = y[0]
		return str(x)
		z = x[1]
		return str(z)

	def intersections(self):
		c = self.a.intersection_update(self.b)
		return str(c)

	def differences(self):
		c = self.b.difference(self.a)
		return str(c)

	def symmetric(self):
		c = self.a.symmetric_difference(self.b)
		sorted(c)
		return str(c)

	def unions(self, a, b, c, d):
		e = a.union(b, c, d)
		return str(e)

	def extends(self, x, y):
		y.extend(x)
		return str(y)


class order:
	def __init__(self, a):
		self.a = a

	def whileloop(self):
		i = 0
		while i<5:
			i+=2
			print(i)

	def sorting(self):
		self.a.append(7)
		self.a.sort()
		return str(self.a)

	def forloop(self):
		i = 0
		for i in self.a:
			print(i)
			i+=1	










# print(add())
# print(remove())
# print(update())
# print(getvalue([1, 2, 3, 4 ,5]))
# print(popval(['a', 'b', 'c', 'd']))
# print(reversing([2, 4, 6, 8]))
# print(counting([1, 2, 3, 4, 5, 6, 7, 8]))
# print(deletingval(["Davao", "Cebu", "Manila", "Butuan"]))
# looping()
# print(check())
# print(length([1, 2, 3, 4, 5, 6]))
# print(multipleset())
# print(intersections({"a", "b", "c", "d"}, {"a", "d", "f"}))
# print(differences({"a", "b", "c", "d"}, {"a", "d", "f"})) 
# print(symmetric({"a", "b", "c", "d"}, {"a", "d", "f"}))
# print(unions())
# print(extends())
# whileloop()
# print(sorting([8, 4, 5, 6]))
# forloop()