from math import *
x = float(input())
y = float(input())
z_first = int((cos(x) ** 4 + sin(y) ** 2 + sin(2 * x) ** 2 / 4 - 1) * 100) / 100
z_second = int((sin(y + x) * sin(y-x) * 100)) / 100
print(z_first, z_second)