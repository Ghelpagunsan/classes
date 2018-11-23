from float import Processes
from float import conditional_statements
from float import random
from float import area



process = Processes(4.5, 5.5)
print(process.addition())
print(process.division())
print(process.multiplication())
print(process.subtraction())

condition = conditional_statements(6.2, 5.6, 6.7)
print(condition.ifstate())
print(condition.elseif())

randoms = random(2.04, 4.6)
print(randoms.whilestate())
print(randoms.floordiv())

area_of_shape = area(12.4, 6.6, 8.3)
print(area_of_shape.rectangle(5.3, 9.2))
print(area_of_shape.circle(4.6))
print(area_of_shape.pyramid(6))
print(area_of_shape.triangle(4.4, 5.7))
print(area_of_shape.cylinder(3.4, 5.9))
print(area_of_shape.tangent(9, 4))
print(area_of_shape.parallel(4.1, 3.2))
print(area_of_shape.trap())
print(area_of_shape.square(6.8))
print(area_of_shape.volume(6.2, 7.7))
print(area_of_shape.cone(5.3, 12.04))