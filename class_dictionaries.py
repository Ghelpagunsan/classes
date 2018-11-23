from dictionaries import crud
from dictionaries import checking
from dictionaries import manipulate
from dictionaries import sets
from dictionaries import create
from dictionaries import display



d = crud({
		"name" : "Gelo",
		"age" : 20 ,
		"city" : "Davao"
		})
print(d.show())
print(d.access())
print(d.change())
print(d.getvals())

checks = checking({
		"breed" : "Pug",
		"weight" : 15 ,
		"gender" : "Male"
		})
print(checks.forloop())
print(checks.check())

edit = manipulate({
		"name" : "Gelo",
		"age" : 20 ,
		"city" : "Davao"
		})
print(edit.add())
print(edit.length())
print(edit.remove())
print(edit.updates())
print(edit.create(("Name", "Age", "City"), 0))

s = sets({
		"name" : "Gelo",
		"age" : 20 ,
		"city" : "Davao",
		"status" : "Single"
		})
print(s.keys())
print(s.default())
print(s.clearing())
print(s.delete({"breed" : "Pug","weight" : 15 ,"gender" : "Male"}))

cr = create(2, 4, 6)
print(cr.dictionary())


show = display({
		"name" : "Gelo",
		"age" : 20 ,
		"city" : "Davao",
		"status" : "Single"
		})
print(show.copies())
print(show.onebyone())
print(show.popitems())
print(show.setdefaults())