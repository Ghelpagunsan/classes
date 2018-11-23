from lists import manipulate
from lists import show
from lists import change
from lists import compare
from lists import order



mani = manipulate(["Toyota", "Suzuki", "Honda"])
print(mani.add())
print(mani.remove())
print(mani.update({"Ford", "Honda", "Suzuki", "Toyota"}))


s = show([1, 2, 3, 4, 5, 6, 7, 8])
print(s.getvalue())
print(s.popval())
print(s.reversing())
print(s.counting())

ch = change([1999, 2000, 2001, 2002, 2003])
print(ch.deletingval())
print(ch.looping())
print(ch.check())


comparing = compare({"a", "b", "c", "d"}, {"a", "d", "f"})
print(comparing.length([1, 2, 3, 4, 5, 6]))
print(comparing.multipleset([((1, 2), (3,4)),(1, 2, 3)]))
print(comparing.intersections())
print(comparing.differences())
print(comparing.symmetric())
print(comparing.unions({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}))
print(comparing.extends(["True", "False"], [1, 0]))


o = order([1, 2, 3, 4, 5])
print(o.whileloop())
print(o.sorting())
print(o.forloop())