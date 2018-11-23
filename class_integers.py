from integers import Operation
from integers import iteration
from integers import comparison
from integers import number



operation = Operation(6, 12)
print(operation.add())
print(operation.subtract(32))
print(operation.multiply())
print(operation.divide(22))
print(operation.cont(23))
print(operation.greater())
print(operation.lesser(10))


item = iteration(3,7)
print(item.recursion(6))
print(item.equal())
print(item.forloop([2,4,6,8]))
print(item.whileloop(4))


compare = comparison(6,12)
print(compare.ifstate())
print(compare.elifstate())
print(compare.swap())


num = number(13)
print(num.insert([1, 2, 3]))
print(num.popnum([2,4,6,8]))
print(num.triangle())
print(num.count([1,1,1,2,2]))
print(num.plainprint())
print(num.convert())