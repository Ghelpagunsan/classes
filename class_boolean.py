from boolean import compute
from boolean import check
from boolean import evaluate



com = compute(10, 15)
print(com.check(32))
print(com.notequal())
print(com.array([1,2,3]))
print(com.add())
print(com.sub())
print(com.prod())
print(com.quo())
print(com.ifst())
print(com.elifst())


look = check(4)
print(look.none())
print(look.string("Time"))
print(look.integer())
print(look.whileloop())


e = evaluate(3)
print(e.expression(8, 8))
print(e.mapping({}))
print(e.forloop([1]))
print(e.float(0.0))
print(e.boolean(False))
print(e.andstate())
print(e.orstate())