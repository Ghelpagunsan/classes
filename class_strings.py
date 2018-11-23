from strings import manipulating
from strings import looping
from strings import compare
from strings import string_array
from strings import changing



control = manipulating("Garden")
print(control.splitting())
print(control.concatenate())
print(control.length())
print(control.position("trinity"))
print(control.whitespace())
print(control.lowercasing())
print(control.uppercasing())



loop = looping("Sadness")
print(loop.forlooping())
print(loop.whilelooping())


com = compare("love", "hate")
print(com.ifstate())
print(com.elifstate())
print(com.range("Moment"))


arr = string_array(["Joy", "Shem", "Van", "Mark"])
print(arr.names())
print(arr.numbering())


ch = changing("Real", "time")
print(ch.replacing("nick"))
print(ch.check(["hi", 5, "me", 4]))
print(ch.counting(["hi", 5, 5, 5, "hello"]))
print(ch.inttostr(234))
print(ch.adding())
print(ch.subtracting())