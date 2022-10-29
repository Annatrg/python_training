from geom2d import *

l1 = [Point(0, 0), Point(3, 2), Point(4, 1)]

l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

print(l1)
print(l2)
