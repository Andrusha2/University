from math import *
r_bottom = float(input())
r_top = float(input())
h = float(input())
s_bottom = pi * r_bottom ** 2
s_top = pi * r_top ** 2
length = sqrt((r_bottom - r_top) ** 2 + h ** 2)
s_side = pi * (r_top + r_bottom) * length
volume = int(((s_bottom + s_top + sqrt(s_bottom * s_top)) * h / 3) * 1000) / 1000
s_total = int((s_bottom + s_top + s_side) * 1000) / 1000

