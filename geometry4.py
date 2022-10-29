

from geom2d import *

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

# оставляем правую ветвь параболы
l2 = list(filter(lambda p: p.x > 0, l))

# где х - четное число
l3 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)
print(l3)
