from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 5)
print(c.r)
