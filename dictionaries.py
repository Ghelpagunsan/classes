	
class crud:
	def __init__(self, d):
		self.d = d

	def show(self):
		return str(self.d)

	def access(self):
		x = self.d.get("age")
		y = self.d["name"]
		return str(str(y) + " , " + str(x))

	def change(self):
		x = self.d["city"] = "Bislig"
		return str(x)

	def getvals(self):
		for x in self.d.values():
			print(x)


class checking:
	def __init__(self, d):
		self.d = d

	def forloop(self): #using the items()
		for x, y in self.d.items():
			print(x, y)

	def check(self):
		if "gender" in self.d:
			return str("Found!")


class manipulate:
	def __init__(self, d):
		self.d = d

	def add(self):
		self.d["status"] = "Single"
		return str(self.d)

	def length(self):
		return str(len(self.d))

	def remove(self):
		self.d.pop("status")
		return str(self.d)

	def updates(self):
		self.d.update({"name":"Ghelo"}) 
		return str(self.d)

	def create(self, x, y):
		d = dict.fromkeys(x)
		return str(d)

class sets:
	def __init__(self, d):
		self.d = d

	def keys(self):
		x = self.d.keys()
		return str(x)

	def default(self):
		x = self.d.setdefault("age", 19)
		return str(x)

	def clearing(self):
		x = self.d.clear()
		return str(x)

	def delete(self, x):
		del x["weight"]
		return str(x)

class create:
	def __init__(self, a, b, c):
		self.a = a
		self.b= b
		self.c = c

	def dictionary(self):
		d = dict(x = self.a, y = self.b, z = self.c)
		return str(d)

class display:
	def __init__(self, d):
		self.d = d

	def copies(self):
		x = self.d.copy()
		return str(x)

	def onebyone(self):
		for x in self.d:
			print(self.d[x])

	def popitems(self): #retieve the popped key and value
		x = self.d.popitem()
		return str(x)

	def setdefaults(self): #other way around
		x = self.d.setdefault("religion", "Christian")
		return str(x)




# print(show())
# print(access())
# print(change())
# getvals()
# forloop()
# print(check())
# print(add())
# print(length())
# print(remove())
# print(updates())
# print(create(("Name", "Age", "City"), 0))
# print(keys())
# print(default())
# print(clearing())
# print(delete())
# print(dictionary())
# print(copies())
# onebyone()
# print(popitems())
# print(setdefaults())

