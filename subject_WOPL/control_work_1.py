from math import *
x = 1
lst = []
while x <= 2:
    lst.append((x, int((cos(x) ** 2) * 1000) / 1000))
    x += 0.45
print(lst)